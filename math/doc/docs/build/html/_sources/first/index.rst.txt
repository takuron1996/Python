.. Pythonで学び直す高校数学（第1章）

コンピュータと数
================================

累乗
------------

.. code-block:: python

   # 10の2乗
   >>> 10 ** 2    
   100

   # 10の-2乗
   >>> 10 ** -2   
   0.1

   # 10の0乗
   >>> 10 ** 0    
   1

基数変換
------------

pythonの標準ライブラリ

.. code-block:: python

   #10進数　→　2進数
   >>> bin(10)    
   '0b1010'

   # 2進数　→　10進数
   >>> int(bin(10), 2)
   10

   #10進数　→　8進数
   >>> oct(10)
   '0o12'

   # 8進数　→　10進数
   >>> int(oct(10), 8)
   10

   #10進数　→　16進数
   >>> hex(18)
   '0x12'

   #16進数　→　10進数
   >>> int(hex(18), 16)
   18  

自作（結果）

.. code-block:: python

   # 10進数 →　2進数   
   26
   26 / 2 = 13 ・・・ 0
   13 / 2 = 6 ・・・ 1 
   6 / 2 = 3 ・・・ 0  
   3 / 2 = 1 ・・・ 1  
   1 / 2 = 0 ・・・ 1  
   11010

   26.625
   26 / 2 = 13 ・・・ 0
   13 / 2 = 6 ・・・ 1 
   6 / 2 = 3 ・・・ 0  
   3 / 2 = 1 ・・・ 1  
   1 / 2 = 0 ・・・ 1  
   0.625 * 2 = 1.25    
   0.25 * 2 = 0.5
   0.5 * 2 = 1.0
   11010.101

   # 10進数　→　8進数
   26
   26 / 8 = 3 ・・・ 2
   3 / 8 = 0 ・・・ 3
   32

   26.625
   26 / 8 = 3 ・・・ 2
   3 / 8 = 0 ・・・ 3
   0.625 * 8 = 5.0
   32.5

   # 10進数　→　16進数
   26
   26 / 16 = 1 ・・・ 10
   1 / 16 = 0 ・・・ 1
   1A

   26.625
   26 / 16 = 1 ・・・ 10
   1 / 16 = 0 ・・・ 1
   0.625 * 16 = 10.0
   1A.A

   # 2進数 →　10進数
   11010
   (1*2**4) + (1*2**3) + (0*2**2) + (1*2**1) + (0*2**0) = 26

   11010.101
   (1*2**4) + (1*2**3) + (0*2**2) + (1*2**1) + (0*2**0) + (1*2**-1) + (0*2**-2) + (1*2**-3) = 26.625

   # 8進数 →　10進数
   32
   (3*8**1) + (2*8**0) = 26

   32.5
   (3*8**1) + (2*8**0) + (5*8**-1) = 26.625

   # 16進数 →　10進数
   1A
   (1*16**1) + (10*16**0) = 26

   1A.A
   (1*16**1) + (10*16**0) + (10*16**-1) = 26.625

python

.. code-block:: python
   :linenos:

   #!/usr/bin/env python3
   # -*- coding: utf_8 -*-
   """
       基数変換の例題プログラム
   """
   
   __author__ = 'Taku Ikegami'
   __version__ = '3.0.1'
   __date__ = '2021/06/06 (Created: 2021/06/05)'
   
   from math import modf
   from os import linesep
   
   
   def radix_conversion_to_dec(target, base_number=2):
       """n進数から10進数に変換（2から16進数まで）
   
       Args:
           target (str)): 基数変換する対象
           base_number (int): 変換元の進数（指定がない場合は2進数、2から16進数）
   
       """
       def pre_calculation(result_list, formula_list):
           """計算準備
           """
           def convert(target):
               """数字をアルファベットに変換
               """
   
               if str.isdigit(target):
                   return target
   
               return ord(target) - ord('A') + 10
   
           def calculation(number, start, stop):
               """計算
               """
               for real, index in zip(number[::-1], range(start, stop)):
                   convert_number = convert(real)
                   result_list.append(
                       int(convert_number) * base_number**int(index))
                   formula_list.append('({}*{}**{})'.format(
                       convert_number, base_number, index))
               return
   
           return calculation
   
       if base_number > 16 or base_number < 2:
           print("2から16進数を指定してください")
           return
   
       print(target)
   
       target_list = target.split('.')
       int_number = target_list[0]
       real_number = ''
       if len(target_list) == 2:
           real_number = target_list[1]
   
       result_list, formula_list = ([], [])
       calculation = pre_calculation(result_list, formula_list)
       calculation(real_number, -len(real_number), 0)
       calculation(int_number, 0, len(int_number))
       result = sum(result_list)
       print('{} = {}'.format(' + '.join(formula_list[::-1]), str(result)) +
             linesep)
   
   
   def radix_conversion_from_dec(dividend, base_number=2):
       """10進数からn進数に変換（2から16進数まで）
   
       Args:
           dividend (float): 基数変換する対象
           base_number (int): 変換先の進数（指定がない場合は2進数、2から16進数）
   
       """
       def convert(number):
           """10以上の数字をアルファベットに変換
           """
           if number < 10:
               return number
   
           return chr(ord('A') + number - 10)
   
       def int_calculation(dividend):
           """整数部分を計算
           """
           result_list = []
           while dividend != 0:
               quotient, remainder = divmod(dividend, base_number)
               print("{} / {} = {} ・・・ {}".format(dividend, base_number, quotient,
                                                  remainder))
               result_list.append(convert(remainder))
               dividend = quotient
           return result_list
   
       def real_calculation(real_number):
           """小数部分を計算
           """
           result_list = []
           count = 0
           while real_number != 0 and count < 10:
               result = real_number * base_number
               print("{} * {} = {}".format(real_number, base_number, result))
               result_list.append(convert(int(result)))
               real_number = result - int(result)
               count += 1
           return result_list
   
       if base_number > 16 or base_number < 2:
           print("2から16進数を指定してください")
           return
   
       print(dividend)
   
       real_number, int_number = modf(dividend)
       int_number = int(int_number)
   
       int_list = int_calculation(int_number)
       real_list = real_calculation(real_number)
   
       template_method = (
           lambda number_list: "".join(map(str, number_list[::-1])))
       int_str = template_method(int_list)
       real_str = template_method(real_list)
       template = "{}".format(int_str) if len(real_str) == 0 else "{}.{}".format(
           int_str, real_str)
       print(template + linesep)
   
   
   def main():
       """
           例題プログラム
       """
       print('# 10進数 →　2進数')
       radix_conversion_from_dec(26, 2)
       radix_conversion_from_dec(26.625, 2)
       print('# 10進数　→　8進数')
       radix_conversion_from_dec(26, 8)
       radix_conversion_from_dec(26.625, 8)
       print('# 10進数　→　16進数')
       radix_conversion_from_dec(26, 16)
       radix_conversion_from_dec(26.625, 16)
   
       print('# 2進数 →　10進数')
       radix_conversion_to_dec('11010', 2)
       radix_conversion_to_dec('11010.101', 2)
       print('# 8進数 →　10進数')
       radix_conversion_to_dec('32', 8)
       radix_conversion_to_dec('32.5', 8)
       print('# 16進数 →　10進数')
       radix_conversion_to_dec('1A', 16)
       radix_conversion_to_dec('1A.A', 16)
   
   
   if __name__ == "__main__":
       main()
     