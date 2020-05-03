#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    2.4 ラベルのエンコーディング
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.1'
__date__ = '2020/5/4'

if __name__ == '__main__':
    """
        ラベルは、単語や数字など様々な形態をとります。
        scikit-learn    ->  機械学習パッケージで、ラベルは数字である必要がある。
        実世界では、ラベルは人間が読める単語の形態をとります。
        これを教師データにするには、単語から数字に対応づけるようにラベル付けします。
        単語のラベルを数字のラベルに変換するには、ラベルのエンコーダを用います。
        ラベルのエンコーディングとは、単語のラベルを数字の形態に変換する処理のことを表します。
        こうして学習アルゴリズムが訓練データを扱えるようになります。
        transform() ->  ラベルを数字に変換
        inverse_transform() ->  数字をラベルに変換
    """
    from sklearn import preprocessing
    
    input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']
    encoder = preprocessing.LabelEncoder()
    encoder.fit(input_labels)
    print('Label mapping:')
    for i, item in enumerate(encoder.classes_):
        print(item, '-->', i)
    
    test_labels = ['green', 'red', 'black']
    encoded_values = encoder.transform(test_labels)
    print('Labels =', test_labels)
    print('Encoded values =', list(encoded_values))
    
    encoded_values = [3, 0, 4, 1]
    decoded_list = encoder.inverse_transform(encoded_values)
    print('Encoded values =', encoded_values)
    print('Decoded labels =', list(decoded_list))
