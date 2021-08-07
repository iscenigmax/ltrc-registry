#!/usr/bin/python
# -*- encoding: utf-8 -*-
import time
import datetime


def get_date_now_for_file():
    return time.strftime("%Y%m%d%H%M%S")


def get_current_year():
    return datetime.date.today().year
