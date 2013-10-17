# -*- coding: utf-8 -*-

#from subprocess import STDOUT, check_call
#import subprocess
import subprocess
#maybe we should make whole new menus? fuk

def startApt(aptarg):
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
		#cfgcurses.curseutil.msg("Please try again", 'red')
		return

def doApt(arg):
	proc = subprocess.Popen(['apt-get %s' % arg, '--force-yes'], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	print "program output:", out
