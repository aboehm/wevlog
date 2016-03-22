#!/usr/bin/python
# -*-: coding: utf-8 -*-
# vim: noexpandtab tabstop=8 shiftwidth=8

import win32evtlog, win32evtlogutil
import sys

def log_msg(prog, event_id, msg_type, message):
	win32evtlogutil.ReportEvent(prog, event_id, eventType=msg_type, strings=[message]) 

def log_info(prog, message):
	log_msg(prog, 0, win32evtlog.EVENTLOG_INFORMATION_TYPE, message)

def log_error(prog, message):
	log_msg(prog, 0, win32evtlog.EVENTLOG_ERROR_TYPE, message)

def log_warning(prog, message):
	log_msg(prog, 0, win32evtlog.EVENTLOG_WARNING_TYPE, message)

def concat_string_array(ar):
	s = ""
	for i in ar:
		s += i + " "

	return s

def help_and_exit():
	print("Windows Event Logger")
	print("Syntax: %s [INFO|ERROR|WARNING] <A message to log>" % (sys.argv[0]))
	sys.exit(0)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		help_and_exit()

	program = sys.argv[0]

	t = sys.argv[1].lower()
	if t == "error":
		if (len(sys.argv) < 3):
			help_and_exit()
		else:
			log_error(program, concat_string_array(sys.argv[2:]))

	elif t == "warning":
		if (len(sys.argv) < 3):
			help_and_exit()
		else:
			log_warning(program, concat_string_array(sys.argv[2:]))

	elif t == "info":
		if (len(sys.argv) < 3):
			help_and_exit()
		else:
			log_info(program, concat_string_array(sys.argv[2:]))

	else:
		log_info(program, concat_string_array(sys.argv[1:]))

	sys.exit(0) 

