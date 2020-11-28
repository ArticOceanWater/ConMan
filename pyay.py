#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from shlex import quote

def install(packages):
    yay("-S",packages)

def search(packages):
    yay("-Ss",packages)

def refresh():
    yay("-Sy")

def update():
    yay("-Syu")

def yay(flags,pkgs):
    exe=["yay","--sudoloop",flags]
    for s in pkgs:
        cmd+=[s]
    subprocess.run(cmd)

