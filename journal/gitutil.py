#!/usr/bin/env python
# -*- coding: utf-8 -*-

from git import Repo


class UserRepo(object):
    def __init__(self, path, emails=None):
        self.repo = Repo(path)
        self.emails = emails or []

    def get_date_commits(self, since, until=None, branches=None):
        date_commits = {}
        if not branches:
            branches = [str(i) for i in self.repo.branches]

        for branch in branches:
            # If we need date comparision then authored_date is the choice
            # as it is smaller or equal to committed_date
            for i in self.repo.iter_commits(branch, since=since, until=until):
                if i.author.email in self.emails:
                    date_commits.setdefault(branch, []).append(i)

        return date_commits
