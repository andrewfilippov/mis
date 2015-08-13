#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  r1.py
#  
#  Copyright 2015 Andrew Filippov <andrew@filippov.by>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import shlex, subprocess


def main(args):
    f = open("np.txt")  # read file like "username@domain password"
    for line in f:
        k = str.split(line)
        subprocess.check_call(["echo", "I will run :", "imapsync --login1", k[0], " --password1 ", k[1]])
    print("Ok")
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
