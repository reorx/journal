#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from git import Repo


repo = Repo('')

today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
tomorrow_midnight = today_midnight + datetime.timedelta(days=1)

for i in repo.iter_commits():
    if i.authored_date < today_midnight:
        break
    i.author
