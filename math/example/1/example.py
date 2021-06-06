#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
    基数変換の例題プログラム
"""

__author__ = 'Taku Ikegami'
__version__ = '2.0.2'
__date__ = '2021/06/06 (Created: 2021/06/05)'


def radix_conversion_to_dec(target, base_number=2):
    """n進数から10進数に変換（2から16進数まで）

    Args:
        target (str)): 基数変換する対象
        base_number (int): 変換元の進数（指定がない場合は2進数、2から16進数）

    """
    def convert(target):
        """数字をアルファベットに変換
        """

        if str.isdigit(target):
            return target

        return ord(target) - ord('A') + 10

    if base_number > 16 or base_number < 2:
        print("2から16進数を指定してください")
        return

    result_list = []
    formula_list = []
    for number, index in zip(target[::-1], range(0, len(target))):
        convert_number = convert(number)
        result_list.append(int(convert_number) * base_number**int(index))
        formula_list.append('({}*{}**{})'.format(convert_number, base_number,
                                                 index))

    result = sum(result_list)
    print('{} = {}'.format(' + '.join(formula_list[::-1]), str(result)))


def radix_conversion_from_dec(dividend, base_number=2):
    """10進数からn進数に変換（2から16進数まで）

    Args:
        dividend (int): 基数変換する対象
        base_number (int): 変換先の進数（指定がない場合は2進数、2から16進数）

    """
    def print_formula(dividend, base_number, quotient, remainder):
        """ 途中式の出力
        """
        template = "{} / {} = {} ・・・ {}"
        print(template.format(dividend, base_number, quotient, remainder))

    def convert(number):
        """10以上の数字をアルファベットに変換
        """
        if number < 10:
            return number

        return chr(ord('A') + number - 10)

    if base_number > 16 or base_number < 2:
        print("2から16進数を指定してください")
        return

    result_list = []

    while dividend != 0:
        quotient, remainder = divmod(dividend, base_number)
        print_formula(dividend, base_number, quotient, remainder)
        result_list.append(convert(remainder))
        dividend = quotient
    print("".join(map(str, result_list[::-1])))


def main():
    """
        例題プログラム
    """
    print('# 10進数 →　2進数')
    radix_conversion_from_dec(26, 2)
    print('# 10進数　→　8進数')
    radix_conversion_from_dec(26, 8)
    print('# 10進数　→　16進数')
    radix_conversion_from_dec(26, 16)

    print('# 2進数 →　10進数')
    radix_conversion_to_dec('11010', 2)
    print('# 8進数 →　10進数')
    radix_conversion_to_dec('32', 8)
    print('# 16進数 →　10進数')
    radix_conversion_to_dec('1A', 16)


if __name__ == "__main__":
    main()
