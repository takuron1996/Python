#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    logクラス
"""

__author__ = 'Taku Ikegami'
__version__ = '0.0.1'
__date__ = '2020/04/24'


class Logger:
    from os import getcwd
    from os.path import join
    
    def __init__(self, name = 'console', conf_filename = join(getcwd(), 'conf', 'conf.yaml')):
        from logging import getLogger
        self._logger = getLogger(name)
        if conf_filename is not None:
            with open(conf_filename) as file:
                from logging.config import dictConfig
                from yaml import load, FullLoader
                dictConfig(load(file.read(), FullLoader))
    
    def debug(self, msg):
        self._logger.debug(msg)
    
    def info(self, msg):
        self._logger.info(msg)
    
    def warn(self, msg):
        self._logger.warning(msg)
    
    def error(self, msg):
        self._logger.error(msg)
    
    def critical(self, msg):
        self._logger.critical(msg)


class ApplicationLogger(Logger):
    def __init__(self, conf_filename = None):
        name='application'
        if conf_filename is None:
            super(ApplicationLogger, self).__init__(name = name)
        else:
            super(ApplicationLogger, self).__init__(name = name, conf_filename = conf_filename)


class EmergencyLogger(Logger):
    
    def __init__(self, conf_filename = None):
        name = 'emergency'
        if conf_filename is None:
            super(EmergencyLogger, self).__init__(name = name)
        else:
            super(EmergencyLogger, self).__init__(name = name, conf_filename = conf_filename)
