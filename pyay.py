#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from shlex import quote

def install(packages):
    pacman("-S",packages)

def search(packages):
    pacman("-Ss",packages)

def pacman(flags,pkgs):
    cmd=["yay","--sudoloop",flags]
    for s in pkgs:
        cmd+=[s]
    subprocess.run(cmd)

