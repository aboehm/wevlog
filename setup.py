#!/usr/bin/python3
# -*-: coding: utf-8 -*-
# vim: noexpandtab tabstop=4 shiftwidth=4

from distutils.core import setup 
import py2exe 
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

setup(
	name = "Windows Event Logger",
	version = "0.0.1",
	author = "Alexander Böhm",
	author_email = "alxndr.boehm@gmail.com",
	description = "Log a given string to Windows Event Log",
	url = "http://infai.org",
	platforms = ["win32"],
    options = {
		"py2exe": {
            "compressed": 1,
            "optimize": 2,
			"includes": [
			],
			"bundle_files": True,
			"dll_excludes": ['w9xpopen.exe'],
        }
    },
	packages = [], 
    zipfile=None,
	console=['wevlog.py'],
)

