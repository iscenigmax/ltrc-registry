#!/usr/bin/python
# -*- encoding: utf-8 -*-
import datetime


def year_choices():
    return [(r, r) for r in range(2015, datetime.date.today().year+1)]

