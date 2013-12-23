#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import string
import datetime
import functools
import subprocess
from workjournal.gitutil import UserRepo


call = functools.partial(subprocess.call, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def create_sample_repo():
    print 'Creating sample repository'
    dirpath = '/tmp/sample_repo' + ''.join([random.choice(string.ascii_letters) for i in range(5)])
    call('mkdir -p %s' % dirpath)
    git_cmds = [
        'cd %s' % dirpath,
        'git init',
        'touch a',
        'git add -A',
        'git commit -m "add a"',
        'touch b',
        'git add -A',
        'git commit -m "add b"',
        'git checkout -b branch1',
        'touch c',
        'git add -A',
        'git commit -m "branch1 add c"',
        'touch d',
        'git add -A',
        'git commit -m "branch1 add d"',
    ]
    call('&&'.join(git_cmds))

    return dirpath


class TestUserRepo(object):
    def setUp(self):
        self.repopath = create_sample_repo()

    def tearDown(self):
        call('rm -rf %s' % self.repopath)

    def test_get_date_commits(self):
        ur = UserRepo(self.repopath)
        print ur.emails
        commit_set = ur.get_date_commits(since=datetime.datetime.now().strftime('%Y-%m-%d'))
        print commit_set
        assert len(commit_set.in_branch('master')) == 2
        assert len(commit_set.in_branch('branch1')) == 4
