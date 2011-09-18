#!/usr/bin/python

import subprocess
import signal
import sys

compass_default = '.'
compass_location = raw_input('Enter the directory for compass to watch (default: {0}): '.format(compass_default))
if not compass_location:
    compass_location = compass_default
compass_args = ['compass', 'watch', "{0}".format(compass_location)]

coffee_default = 'script.coffee'
coffee_location = raw_input('Enter the file location for coffee to watch (default: {0}): '.format(coffee_default))
if not coffee_location:
    coffee_location = coffee_default
coffee_args = ['coffee', '--watch', '--compile', "{0}".format(coffee_location)]

server_use = raw_input('Use server? (y|n) (default: yes): ')
if server_use in ['y', 'yes', 'true', 'True'] or not server_use:
    server_use = True
    server_args = ['python', '-m', 'SimpleHTTPServer']
    server_process = subprocess.Popen(server_args)
else:
    server_use = False

compass_process = subprocess.Popen(compass_args)
coffee_process = subprocess.Popen(coffee_args)

def signal_handler(signal, frame):
    compass_process.terminate()
    coffee_process.terminate()
    if server_use:
        server_process.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
