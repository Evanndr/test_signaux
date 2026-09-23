#!/usr/bin/python3
import signal as sig
from time import sleep
import sys
import os
import random
import subprocess

PID_J1 = os.getpid()
FILE_J1 = "/tmp/j1.pid"
FILE_J2 = "/tmp/j2.pid"

print("pid=", os.getpid(), x)

def pierre(s, frame):
	print( "réception du signal ", sig.Signals(s).name )


def feuille(s, frame):
	print( "réception du signal ", sig.Signals(s).name )


def ciseaux(s, frame):
	print( "réception du signal ", sig.Signals(s).name )



while True:
	sig.signal(sig.SIGUSR1, pierre)
	sig.signal(sig.SIGUSR2, feuille)
	sig.signal(sig.SIGINT, ciseaux)
	choix = random.randint(0, 2)
	sleep(1)








