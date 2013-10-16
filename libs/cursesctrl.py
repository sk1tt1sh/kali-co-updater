# -*- coding: utf-8 -*-
"""
This lib will contain all the pretty graphical crap for curses.
Initialization of screen settings.
Background and text schnazzy colors
Menu functionality
"""

import curses
from curses import panel
#import aptgets

scr = curses.initscr()
colors = {
		'red': 1, 'white': 2, 'magenta': 3, 'green': 4, 'blue': 5
			}

def endcrs():
	curses.endwin()

def aptupdate():
	aptgets.startApt('1')

class curseutil():
	_instance = None

	def __init__(self):
		try:
			scr.keypad(1)
			curses.start_color()
			curses.curs_set(0)
			curses.cbreak()
			curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
			curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
			curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
			curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
			curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLUE)
		except Exception, e:
			print "Error: %s" % e
			curses.endwin()

	def message(self, text, txcolor):
		scr.addstr(text, curses.color_pair(colors[txcolor]))

	def waitinpt(self):
		while 1:
			self.message("Waiting for something to happen....", 'white')
			key = scr.getch()  # Get press key
			if key == ord("q"):
				break
		endcrs()


class cursemenu(object):

	def __init__(self, item):
		self.window = scr.subwin(0,0)
		self.window.keypad(1)
		self.panel = panel.new_panel(self.window)
		self.panel.hide()
		panel.update_panels()

		self.position = 0
		self.items = item
		self.items.append(('exit', endcrs()))

	def navigate(self, nloc):
		self.position += nloc
		if self.position < 0:
			self.position = 0
		elif self.position >= len(self.items):
				self.position = len(self.items)-1

	def display(self):
		self.panel.top()
		self.panel.show()
		self.window.clear()

		while True:
			self.window.refresh()
			curses.doupdate()
			for index, item in enumerate(self.items):
				if index == self.position:
					mode = curses.A_REVERSE
				else:
					mode = curses.A_NORMAL

				msg = '%d. %s' % (index, item[0])
				self.window.addstr(1+index, 1, msg, mode)

			key = self.window.getch()

			if key in [curses.KEY_ENTER, ord('\n')]:
				if self.position == len(self.items)-1:
					break
				else:
					self.items[self.position][1]

			elif key == curses.KEY_UP:
				self.navigate(-1)

			elif key == curses.KEY_DOWN:
				self.navigate(1)

		self.window.clear()
		self.panel.hide()
		panel.update_panels()
		curses.doupdate()
		endcrs()