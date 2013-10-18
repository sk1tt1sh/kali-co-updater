# -*- coding: utf-8 -*-

#import subprocess
from time import sleep
from os import system


def startApt(aptarg):
	system('reset')
	if aptarg == 1:
		arg = 'update'
		doApt(arg)
	elif aptarg == 2:
		arg = 'upgrade'
		doApt(arg)
	elif aptarg == 3:
		arg = 'upgrade -f'
		doApt(arg)
	elif aptarg == 4:
		arg = 'dist-upgrade'
		doApt(arg)
	elif aptarg == 1234:
		doAllApt()
	else:
		return(1)

def doApt(arg):
	system('apt-get %s -y' % arg)
	print "Chillin for a sec so you can review the exec..."
	sleep(5)
	return

def doAllApt():
	system('apt-get update -y && apt-get upgrade -y && apt-get dist-upgrade -y')
	print "Alllll done. Sleeping 10 sec for you to see what happened"
	sleep(5)
	return