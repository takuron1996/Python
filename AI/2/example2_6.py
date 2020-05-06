#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    2.6 単純ベイズ分類器
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.1'
__date__ = '2020/05/04'

if __name__ == '__main__':
    """
        単純ベイズは、ベイズの定理に基づいて分類器を構築する手法です。
        ベイズの定理とは、ある事象に関連する様々な条件のもとで起こる事象の確率を記述します。
    """
    import numpy as np
    from sklearn.naive_bayes import GaussianNB
    from AI.lib.utilities import visualize_classifier
    
    input_file = 'data_multivar_nb.txt'
    data = np.loadtxt(input_file, delimiter = ',')
    x, y = data[:, :-1], data[:, -1]
    classifier = GaussianNB()
    classifier.fit(x, y)
    y_pred = classifier.predict(x)
    
    accuracy = 100.0 * (y == y_pred).sum() / x.shape[0]
    visualize_classifier(classifier, x, y,
                         title = 'Accuracy of Naive Bayes classifier =' + str(round(accuracy, 2)) + '%')
    
    from sklearn import model_selection
    
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size = 0.2, random_state = 3)
    
    classifier_new = GaussianNB()
    classifier_new.fit(x_train, y_train)
    y_test_pred = classifier_new.predict(x_test)
    
    accuracy = 100.0 * (y_test == y_test_pred).sum() / x_test.shape[0]
    visualize_classifier(classifier_new, x_test, y_test,
                         title = 'Accuracy of the new classifier =' + str(round(accuracy, 2)) + '%')
    
    num_folds = 3
    accuracy_values = model_selection.cross_val_score(classifier, x, y, scoring = 'accuracy', cv = num_folds)
    print('Accuracy: ' + str(round(100 * accuracy_values.mean(), 2)) + '%')
