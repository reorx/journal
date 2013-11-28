#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from git import Repo


repo = Repo('/home/reorx/workspace/lab/cc')

today_start = datetime.datetime.now().replace(hour=6, minute=0, second=0, microsecond=0)

#for i in repo.iter_commits():
    #if i.authored_date < today_midnight:
        #break
    #i.author

print dir(repo)
print 'on migration'
for i in repo.iter_commits('migration'):
    print type(i.author), i.committed_date >= i.authored_date
print i.author
