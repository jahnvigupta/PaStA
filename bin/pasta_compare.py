#!/usr/bin/env python3

"""
PaStA - Patch Stack Analysis

Copyright (c) OTH Regensburg, 2016

Author:
  Ralf Ramsauer <ralf.ramsauer@othr.de>

This work is licensed under the terms of the GNU GPL, version 2.  See
the COPYING file in the top-level directory.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PaStA import *


def compare(commits):
    for i in range(len(commits)-1):
        commit_a = commits[i]
        commit_b = commits[i+1]

        show_commits(commit_a, commit_b)

        rating = preevaluate_two_commits(commit_a, commit_b)
        if rating:
            print('Preevaluation: Possible candidates')
            rating = evaluate_commit_pair(config.thresholds, commit_a, commit_b)
            print(str(rating.msg) + ' message and ' +
                  str(rating.diff) + ' diff, diff length ratio: ' +
                  str(rating.diff_lines_ratio))
        else:
            print('Preevaluation: Not related')
        getch()

if __name__ == '__main__':
    compare(sys.argv[1:])