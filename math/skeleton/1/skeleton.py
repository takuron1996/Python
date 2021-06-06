#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
    基数変換の例題プログラム
        基数変換のプログラムをPythonの標準ライブラリを使用せずに作成せよ
        （途中式を出力すること）
            Pythonの標準ライブラリ（使用してはいけないライブラリ）
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
            ヒント
                # 10の2乗
                >>> 10 ** 2
                100

                # 10の-2乗
                >>> 10 ** -2
                0.1

                # 10の0乗
                >>> 10 ** 0
                1

                # 商の求め方
                >>> 10 // 3
                2

                # 余りの求め方
                >>> 10 % 3
                1

                # 商と余りの求め方
                >>> divmod(10, 3)
                (3, 1)

    問題1-1
        10進数から2進数へ変換するプログラムを自作せよ
    
    問題1-2
        10進数から8進数へ変換するプログラムを自作せよ
    
    問題1-3
        10進数から16進数へ変換するプログラムを自作せよ
    
    問題2-1
        2進数から10進数へ変換するプログラムを自作せよ
    
    問題2-2
        8進数から10進数へ変換するプログラムを自作せよ
    
    問題2-3
        16進数から10進数へ変換するプログラムを自作せよ

    解答（実行結果）
        # 10進数 →　2進数
        26 / 2 = 13 ・・・ 0
        13 / 2 = 6 ・・・ 1
        6 / 2 = 3 ・・・ 0
        3 / 2 = 1 ・・・ 1
        1 / 2 = 0 ・・・ 1
        11010
        # 10進数　→　8進数
        26 / 8 = 3 ・・・ 2
        3 / 8 = 0 ・・・ 3
        32
        # 10進数　→　16進数
        26 / 16 = 1 ・・・ 10
        1 / 16 = 0 ・・・ 1
        1A
        # 2進数 →　10進数
        (1*2**4) + (1*2**3) + (0*2**2) + (1*2**1) + (0*2**0) = 26
        # 8進数 →　10進数
        (3*8**1) + (2*8**0) = 26
        # 16進数 →　10進数
        (1*16**1) + (10*16**0) = 26

"""

__author__ = 'Taku Ikegami'
__version__ = '2.0.2'
__date__ = '2021/06/06 (Created: 2021/06/05)'


def radix_conversion_to_dec(target, base_number):
    """問題2 n進数から10進数に変換（2から16進数まで）

    Args:
        target (str)): 基数変換する対象
        base_number (int): 変換元の進数（指定がない場合は2進数、2から16進数）

    """
    def convert(target):
        """数字をアルファベットに変換
        """
        # 16進数の変換に必要
        pass

    if base_number > 16 or base_number < 2:
        print("2から16進数を指定してください")
        return


    # 問題2-1 から 2-3 はここに作成
    pass


def radix_conversion_from_dec(dividend, base_number=2):
    """問題1 10進数からn進数に変換（2から16進数まで）

    Args:
        dividend (int): 基数変換する対象
        base_number (int): 変換先の進数（指定がない場合は2進数、2から16進数）

    """
    def print_formula(dividend, base_number, quotient, remainder):
        """ 途中式の出力
        """
        # 途中式の出力で使用（任意）
        pass

    def convert(number):
        """10以上の数字をアルファベットに変換
        """
        # 16進数の変換に必要
        pass

    if base_number > 16 or base_number < 2:
        print("2から16進数を指定してください")
        return

    # 問題1-1 から 1-3 はここに作成
    pass


def main():
    """
        例題プログラム
    """
    #問題1　10進数からn進数への変換
    print('# 10進数 →　2進数')
    radix_conversion_from_dec(26, 2)
    print('# 10進数　→　8進数')
    radix_conversion_from_dec(26, 8)
    print('# 10進数　→　16進数')
    radix_conversion_from_dec(26, 16)

    #問題2 n進数から10進数への変換
    print('# 2進数 →　10進数')
    radix_conversion_to_dec('11010', 2)
    print('# 8進数 →　10進数')
    radix_conversion_to_dec('32', 8)
    print('# 16進数 →　10進数')
    radix_conversion_to_dec('1A', 16)


if __name__ == "__main__":
    main()
