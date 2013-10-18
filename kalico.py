#!/usr/bin/env python

"""
	KaliCoUpdater uses cures for interactivity. A primary goal is
	quick-no-reading easy use!
	Plugins are an intended item in the future. Startup tricks will
	be added as well.
	i.e. you can add certain options to start services and updates at startup!
	----------------------
	This is the primary script. All requests to others will come from here
	Everything is try-except because of curses
	----------------------
	title: KaliCombinedUpdate
	author: sk1tt1sh
	Date Created: 02-10-2013
"""
from curses import wrapper
from libs import menus
from os import system

def startup():
	if __name__ == '__main__':
		wrapper(menus.menus)

startup()
system('reset')
exit()