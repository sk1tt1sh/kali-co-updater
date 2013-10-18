# -*- coding: utf-8 -*-

from aptgets import startApt
from gitpulls import startGit


class runupdate:

	def __init__(self, updateargs):
		self.args = 0
		self.args = updateargs

	def parsecmd(self):
		if self.args != 0:
			if self.args <= 4 or self.args == 1234:
				startApt(self.args)
				return
			elif self.args == 5:
				startGit(self.args)
			elif self.args == 6:
				startGit(self.args)
			elif self.args == 7:
				startGit(self.args)
		else:
			print "b0rked..."
			return