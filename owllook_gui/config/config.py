#!/usr/bin/env python
"""
 Created by howie.hu at 2018/6/4.
"""
import logging
import os

logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

logging.basicConfig(
    format=logging_format,
    level=logging.DEBUG
)


class Config:
    APP_TITLE = 'owllook 小说监控'
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    LOGGER = logging.getLogger()
