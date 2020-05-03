#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    2.3 データの前処理
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.1'
__date__ = '2020/5/3'

if __name__ == '__main__':
    from os import linesep
    import numpy as np
    from sklearn import preprocessing
    
    input_data = np.array([[5.1, -2.9, 3.3], [-1.2, 7.8, -6.1], [3.9, 0.4, 2.1], [7.3, -9.9, -4.5]])
    
    # 2.3.1 二直化
    """
        input_dataの2.1を超える値は1になり、それ以下は0になる。
            [[ 5.1 -2.9  3.3]
            [-1.2  7.8 -6.1]
            [ 3.9  0.4  2.1]
            [ 7.3 -9.9 -4.5]]
        が
            [[1. 0. 1.]
            [0. 1. 0.]
            [1. 0. 0.]
            [1. 0. 0.]]
        となる
    """
    data_binarized = preprocessing.Binarizer(threshold = 2.1).transform(input_data)
    print('Binarized data:{} {}'.format(linesep, data_binarized))
    
    # 2.3.2 平均値を引く
    """
        平均値を引くのは、機械学習で一般的に使用される前処理方法。
        特徴ベクトルから平均を引くと、特徴量の中心が原点になる。
        特徴ベクトルからバイアスを除去するために、平均値を引く。
        mean()  ->  平均(Mean)
        std()   ->  標準偏差(Std deviation)
        scale() ->  平均値を引いてから、標準偏差が1になるようにスケーリング
    """
    print("BEFORE:")
    print(" Mean =", input_data.mean(axis = 0))
    print(" Std deviation =", input_data.std(axis = 0))
    
    data_scaled = preprocessing.scale(input_data)
    print("AFTER:")
    print(" Mean =", data_scaled.mean(axis = 0))
    print(" Std deviation =", data_scaled.std(axis = 0))
    
    data_centered = preprocessing.scale(input_data, with_std = False)
    print("CENTER:")
    print(" Mean =", data_centered.mean(axis = 0))
    print(" Std deviation =", data_centered.std(axis = 0))
    
    # 2.3.3 スケーリング
    """
        特徴ベクトルの各特徴量の値は、様々な値を取り得る。
        機械学習アルゴリズムの訓練に使える水準に合うように、特徴量の値を
        スケーリングすることが重要。
        測定値の性質上、不自然に値を大きくしたり小さくしたりしてはいけない。
        値域[0,1]を指定して最大値と最小値に収まるようにデータをスケーリングする。
        スケーリングされると最小値が0、最大値が1で他の値は相対値になる。
    """
    data_scaler_minmax = preprocessing.MinMaxScaler(feature_range = (0, 1))
    data_scaler_minmax = data_scaler_minmax.fit_transform(input_data)
    print('Min max scaled data:{}{}'.format(linesep, data_scaler_minmax))
    
    # 2.3.4 正規化
    """
        特徴ベクトルの値を共通的な尺度に揃えることを正規化(normalization)という。
        最も一般的な正規化手法は、ベクトルの要素のの絶対値の和が1になるようにしたL1正規化です。
        つまり最小絶対値(least absolute deviations)を参照して、各行において絶対値の和が1となるように調整します。
        一方、L2正規化は、各行の要素の自乗の和が1となるようにします。
        一般に、L1正規化はL2正規化よりもロバストであると考えられている。
        L1正規化は、データの外れ値の影響を受けにくいためである。
        データに外れ値が含まれていても、どうすることもできない場合がよくある。
        計算中に外れ値を安全かつ効率的に無視できる手法を選ぶと良い。
        一方、外れ値も重要になる問題を解く場合には、L2正規化を選ぶ方がよい。
        normalize() ->  normで指定した正規化を行う関数
    """
    data_normalized_l1 = preprocessing.normalize(input_data, norm = 'l1')
    data_normalized_l2 = preprocessing.normalize(input_data, norm = 'l2')
    print('L1 normalized data:{}{}'.format(linesep, data_normalized_l1))
    print('L2 normalized data:{}{}'.format(linesep, data_normalized_l2))
