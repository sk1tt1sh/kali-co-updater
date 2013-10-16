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
	author: x1n1x
	Date Created: 02-10-2013
"""

from libs import cursesctrl
from libs import menus
from time import sleep

crs = cursesctrl.curseutil()


def startup():
	menus.display()
	# Once we leave menu lets just exit for now. Menu will be where the magic happens
	endprog()


def endprog():
	crs.message("Ended!...", 'red')
	sleep(1)
	cursesctrl.endcrs()


print "Started..."
startup()
print "should have seen something"
endprog()
exit()