# -*- coding: utf-8 -*-
# right_justify.py


def right_justify(s):
    l = len(s)
    slen = 69 - l
    print(' '*slen, s)


s = "modify"
right_justify(s)
