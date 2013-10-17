# -*- coding: utf-8 -*-
import ucparse
import curses
from curses import panel

colors = {
		'red': 1, 'white': 2, 'magenta': 3, 'green': 4, 'blue': 5
			}

none = ""


class cursemenu(object):

	def __init__(self, passedmenu, stdscreen):
		self.window = stdscreen.subwin(0, 0)
		self.window.keypad(1)

		curses.start_color()
		curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
		curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
		curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLUE)

		self.panel = panel.new_panel(self.window)
		self.panel.hide()
		panel.update_panels()

		self.position = 0
		self.items = passedmenu
		self.items.append(('exit', 'exit'))

	def message(self, text, txcolor):
		self.window.addstr(text, curses.color_pair(colors[txcolor]))

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
					self.items[self.position][1]()

			elif key == curses.KEY_UP:
				self.navigate(-1)

			elif key == curses.KEY_DOWN:
				self.navigate(1)

		self.window.clear()
		self.panel.hide()
		panel.update_panels()
		curses.doupdate()




class menus(object):

	def __init__(self, stdscreen):
		self.screen = stdscreen
		curses.curs_set(0)

		aptupdate = '1'
		updateapt = ucparse.runupdate(aptupdate)

		aptupgrade= '2'
		upgradeapt= ucparse.runupdate(aptupgrade)

		aptitude_items = [
				("Update apt lists", updateapt.parsecmd),
				("Upgrade apt apps", upgradeapt.parsecmd)
				]
		aptmenu = cursemenu(aptitude_items, self.screen)

		gitmenu_items = [
				("pull known git repos(Unimprement)", 'none')
				]
		gitmenu = cursemenu(gitmenu_items, self.screen)

		main_menu_items = [
				("Manage aptitude", aptmenu.display),
				("Manage cloned gits", gitmenu.display)
				]
		main_menu = cursemenu(main_menu_items, self.screen)

		main_menu.display()

