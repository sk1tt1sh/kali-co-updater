# -*- coding: utf-8 -*-

import subprocess
from os import system

# Need to read GIT directories in path for updates

def startGit(gitarg):
	system('reset')
	if gitarg == 5:
		doGit('pull')
	elif gitarg == 6:
		gitarg = raw_input('Please enter repo addr: ')
		gitarg2 = raw_input('Please enter directory to clone to: ')
		doGClone(gitarg, gitarg2)
	elif gitarg == 7:
		# Need to add database functionality for this.
		# For now write the path to a file
		gitPath = raw_input('Enter the path where you clone to: ')
		doAddPath(gitPath)
	else:
		print "Not a git arg!!!"
		return(1)

def doGit(gitarg):
	proc = subprocess.Popen(['git %s' % gitarg], stdout=subprocess.PIPE)
	(out, err) = proc.communicate()
	print out
	return

def doGClone(gitarg, gitarg2):
	return
def doAddPath(gitPath):
	return