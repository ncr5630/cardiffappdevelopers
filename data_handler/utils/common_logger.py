# -*- coding: utf-8 -*-
# !/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
import logging
import logging.handlers
import datetime
from datetime import timedelta, date, datetime
from xmlrpc.client import boolean


class CommonLogger():
    def __init__(self, level, cus_message=None, sys_message=None, class_name=None) -> str:
        self.loginfo = True
        self.am_logger = None
        self.log_filename = None
        date_time_obj = datetime.now()
        self.log_datetime = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        self.level = level
        self.cus_message = cus_message
        self.sys_message = sys_message
        self.class_name = class_name
        self._manage_logger()

    def _manage_logger(self) -> boolean:
        return_val = True
        level = self.level
        loginfo = self.loginfo
        if self.cus_message or self.sys_message:
            logging_message = "Custom_message : %s, System_message:%s, Class_name:%s" % ( \
                self.cus_message, self.sys_message, self.class_name)
            am_logger = logging.getLogger('gunicorn.error')
            if level == "info" and loginfo:
                am_logger.setLevel(logging.DEBUG)
                am_logger.info(logging_message)

            elif level == "warning":
                am_logger.setLevel(logging.WARNING)
                am_logger.warning(logging_message)

            elif level == "error":
                am_logger.setLevel(logging.ERROR)
                am_logger.error(logging_message)

            elif level == "critical":
                am_logger.setLevel(logging.CRITICAL)
                am_logger.critical(logging_message)
        return return_val
