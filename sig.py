#!/usr/bin/python3
import signal as sig
from time import sleep
import sys
import os

def signal_handler(s, frame):
	print( "réception du signal ", sig.Signals(s).name )
	sys.exit()


def signal_handler2(s, frame):
        print( "réception du signal ", sig.Signals(s).name )


sig.signal(sig.SIGINT, signal_handler)
sig.signal(sig.SIGQUIT, signal_handler2)


x=1
while True:
	print("pid=", os.getpid(), x)
	sleep(.5)
	x += 1

