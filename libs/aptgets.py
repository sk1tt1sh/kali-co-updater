# -*- coding: utf-8 -*-

import subprocess
from os import system


def startApt(aptarg):
	system('reset')
	if aptarg == '1':
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
	else:
		return

def doApt(arg):
	proc = subprocess.Popen(['apt-get %s' % arg, '--force-yes'], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print out
	return