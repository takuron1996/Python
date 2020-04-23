#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    ログのテンプレート
"""

__author__ = 'Taku Ikegami'
__version__ = '1.0.1'
__date__ = ''


def main():
    """
        ログのexampleを実行
    """
    from practice.log.logger import Logger, ApplicationLogger, EmergencyLogger
    logger = Logger()
    logger.debug('debug')
    logger.info('info')
    logger.warn('warn')
    logger.error('error')
    logger.critical('critical')
    logger = ApplicationLogger()
    logger.debug('debug')
    logger.info('info')
    logger.warn('warn')
    logger.error('error')
    logger.critical('critical')
    logger = EmergencyLogger()
    logger.debug('debug')
    logger.info('info')
    logger.warn('warn')
    logger.error('error')
    logger.critical('critical')
    return 0


if __name__ == '__main__':
    """
        main関数を実行
    """
    main()
