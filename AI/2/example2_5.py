#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    2.5 ロジスティック回帰による分類器
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.1'
__date__ = '2020/05/04'

if __name__ == '__main__':
    """
          ロジスティック回帰は、入力変数と出力変数の間の関係を説明するのに使用される手法のひとつです。
        入力変数は互いに独立であり、出力変数は従属変数であると仮定します。
        出力変数は、決まった値の集合うちからひとつの値を取るとします。
        この値が分類問題のクラスに対応するわけです。
          目標は、ロジスティック関数を用いて確率を推定することによって、入力変数と出力変数の間の関係性を見つけ出すことです。
        ロジスティック関数はシグモイド曲線(sigmoid curve)であり、いくつかのパラメータを使って関数を構成します。
        ロジスティック回帰は、点群の誤差を最小にする直線を当てはめる一般化線形モデル解析に密接に関係しています。
        今回は、線形回帰の代わりにロジスティック回帰を用います。
        ロジスティック回帰自体は分類手法ではないが、出力変数を固定値にすることによって、分類問題の解法として使用します。
        ロジスティック回帰は単純なので、機械学習でごく普通に使用されます。
    """
    import numpy as np
    from sklearn import linear_model
    
    x = np.array(
        [
            [3.1, 7.2], [4, 6.7], [2.9, 8], [5.1, 4.5], [6, 5], [5.6, 5], [3.3, 0.4], [3.9, 0.9],
            [2.8, 1], [0.5, 3.4], [1, 4], [0.6, 4.9]
        ]
    )
    y = np.array(
        [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    )

    classifier = linear_model.LogisticRegression(solver = 'liblinear', C = 1, multi_class = 'auto')
    # classifier = linear_model.LogisticRegression(solver = 'liblinear', C = 100, multi_class = 'auto')
    classifier.fit(x, y)
    
    from AI.lib.utilities import visualize_classifier
    
    visualize_classifier(classifier, x, y)