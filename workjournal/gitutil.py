#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from git import Repo


class UserRepo(object):
    def __init__(self, path, emails=None):
        self.repo = Repo(path)
        self.emails = emails or []

    @property
    def branches(self):
        return [str(i) for i in self.repo.branches]

    def get_date_commits(self, since, until=None, branches=None):
        commit_set = CommitSet(self)
        if not branches:
            branches = self.branches

        logging.debug('branches: %s', branches)

        for branch in branches:
            # If we need date comparision then authored_date is the choice
            # as it is smaller or equal to committed_date
            for i in self.repo.iter_commits(branch, since=since, until=until):
                logging.debug('commit message: %s', i.message)
                if i.author.email in self.emails:
                    commit_set.add(i, branch)

        return commit_set


class CommitSet(object):
    def __init__(self, user_repo):
        self.user_repo = user_repo
        self.commits = []

    def add(self, commit, branch):
        item = self.get(commit.hexsha)
        if item:
            item[1].add(branch)
        else:
            self.commits.append((commit, {branch}))

    def get(self, hexsha):
        for i in self.commits:
            if i[0].hexsha == hexsha:
                return i
        return None

    def branch_commits(self):
        d = {}
        for i in self.commits:
            for branch in i[1]:
                d.setdefault(branch, []).append(i[0])
        return d

    def in_branch(self, branch):
        l = []
        for i in self.commits:
            if branch in i[1]:
                l.append(i[0])
        return l

    def __str__(self):
        return '<CommitSet: %s commits>' % len(self.commits)
