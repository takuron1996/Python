#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    可視化用の関数
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.1'
__date__ = '2020/05/04'

from sklearn.linear_model import LogisticRegression


def visualize_classifier(classifier: LogisticRegression, x, y, title = ''):
    """
    可視化の関数
    :type classifier: LogisticRegression
    :param classifier: 分類器オブジェクト
    :param x: 入力データ
    :param y: ラベル
    :param title: 図のタイトル
    :return:
    """
    import numpy as np
    import matplotlib.pyplot as plt
    
    min_x, max_x = x[:, 0].min() - 1.0, x[:, 0].max() + 1.0
    min_y, max_y = x[:, 1].min() - 1.0, x[:, 1].max() + 1.0
    mesh_step_size = 0.01
    
    x_vals, y_vals = np.meshgrid(
        np.arange(min_x, max_x, mesh_step_size),
        np.arange(min_y, max_y, mesh_step_size)
    )
    
    output = classifier.predict(np.c_[x_vals.ravel(), y_vals.ravel()])
    output = output.reshape(x_vals.shape)
    
    plt.figure()
    plt.title(title)
    plt.pcolormesh(x_vals, y_vals, output, cmap = plt.cm.gray)
    plt.scatter(x[:, 0], x[:, 1], c = y, s = 75, edgecolors = 'black', linewidths = 1, cmap = plt.cm.Paired)
    
    plt.xlim(x_vals.min(), x_vals.max())
    plt.ylim(y_vals.min(), y_vals.max())
    plt.xticks(
        (np.arange(int(min_x), int(max_x), 1.0))
    )
    plt.yticks(
        (np.arange(int(min_y), int(max_y), 1.0))
    )
    
    plt.show()
