# -*- coding: utf-8 -*-
# Created by restran on 2016/12/4 / Edited by William Khepri on 2018/02/08
from __future__ import unicode_literals, absolute_import

# https://es.wikipedia.org/wiki/ROT13

"""
 ROT13 Una variación del cifrado Cesar usado en la Antigua Roma.
"""


def main(data):
    buff = ""
    for i in data:
        if i in "{}_1234567890":
            buff += i
        elif ord('A') <= ord(i) <= ord('Z'):
            buff += chr((ord(i) - 13 + 26 - ord('A')) % 26 + ord('A'))
        else:
            buff += chr((ord(i) - 13 + 26 - ord('a')) % 26 + ord('a'))
        print(buff)


if __name__ == '__main__':
    input_data = "synt{mur_VF_syn9_svtug1at}"
    main(input_data)
