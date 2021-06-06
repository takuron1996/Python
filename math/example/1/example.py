#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
    基数変換の例題プログラム
"""

__author__ = 'Taku Ikegami'
__version__ = '3.0.1'
__date__ = '2021/06/06 (Created: 2021/06/05)'

from math import modf


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
    print('{} = {}'.format(' + '.join(formula_list[::-1]), str(result)))


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

    real_number, int_number = modf(dividend)
    int_number = int(int_number)

    int_list = int_calculation(int_number)
    real_list = real_calculation(real_number)

    template_method = (
        lambda number_list: "".join(map(str, number_list[::-1])))
    int_str = template_method(int_list)
    real_str = template_method(real_list)
    template = "{}".format(int_str)
    if len(real_str) != 0:
        template = "{}.{}".format(int_str, real_str)
    print(template)


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
    radix_conversion_to_dec('11010.101', 2)
    print('# 8進数 →　10進数')
    radix_conversion_to_dec('32.5', 8)
    print('# 16進数 →　10進数')
    radix_conversion_to_dec('1A.A', 16)


if __name__ == "__main__":
    main()
