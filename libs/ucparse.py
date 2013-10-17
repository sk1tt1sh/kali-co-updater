# -*- coding: utf-8 -*-

from aptgets import startApt


class runupdate:

	def __init__(self, updateargs):
		self.args = 0
		self.args = updateargs

	def parsecmd(self):
		if self.args != 0:
			startApt(self.args)
			return
		else:
			print "b0rked..."
			return