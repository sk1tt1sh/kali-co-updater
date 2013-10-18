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
		self.listlen = len(self.items)
		self.items.append(('exit', 'exit'))

	def message(self, text, txcolor):
		self.window.addstr(text, curses.color_pair(colors[txcolor]))

	def navigate(self, nloc):
		self.position += nloc
		if self.position < 0:
			self.position = 0
		elif self.position >= len(self.items):
				self.position = len(self.items)-1

	def jumpnav(self, jloc):
		self.position = jloc
		if self.position < 0:
			self.position = 0
		elif self.position >= len(self.items):
				self.position = len(self.items)-1

	def display(self):
		self.window.keypad(1)
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
					self.panel.hide()
					curses.def_prog_mode() # Save state
					self.items[self.position][1]()
					curses.reset_prog_mode() # reset to 'current' curses environment
					curses.curs_set(1) # reset doesn't do this right
					curses.curs_set(0)
					self.panel.top()
					self.panel.show()
					self.window.clear()

			elif key == curses.KEY_UP:
				self.navigate(-1)

			elif key == curses.KEY_DOWN:
				self.navigate(1)

			elif key != 258 and key != 259 and key in range(48, 58, 1):
				self.jumpnav(key-48)

		self.window.clear()
		self.panel.hide()
		panel.update_panels()
		curses.doupdate()


class menus(object):

	def __init__(self, stdscreen):
		self.screen = stdscreen
		curses.noecho()
		curses.curs_set(0)

		updateapt = ucparse.runupdate(1)
		upgradeapt = ucparse.runupdate(2)
		upgradefapt = ucparse.runupdate(3)
		distupgrade = ucparse.runupdate(4)
		doallapt = ucparse.runupdate(1234)
		gitpull = ucparse.runupdate(5)
		gitclone = ucparse.runupdate(6)

		aptitude_items = [
				("Update apt lists", updateapt.parsecmd),
				("Upgrade apt apps", upgradeapt.parsecmd),
				("Upgrade and fix dependancies (can take a while)", upgradefapt.parsecmd),
				("Do dist-upgrade", distupgrade.parsecmd),
				("Do them all! (Does not fix dependancies)", doallapt.parsecmd)
				]
		aptmenu = cursemenu(aptitude_items, self.screen)

		gitmenu_items = [
				("Pull known git repos", gitpull.parsecmd),
				("Clone a git", gitclone.parsecmd),
				("Enter git custom repo path (script assumes /opt/", 'none')
				]
		gitmenu = cursemenu(gitmenu_items, self.screen)

		service_items = [
				("List non-standard services. (Assumes Kali)", 'exit'),
				("Enable service", 'exit'),
				("Disable service", 'exit'),
				("Auto start a service", 'exit'),
				("Stop autostart of a service", 'exit')
				]
		servicemenu = cursemenu(service_items, self.screen)

		main_menu_items = [
				("Manage aptitude", aptmenu.display),
				("Manage cloned gits", gitmenu.display),
				("Service control", servicemenu.display)
				]
		main_menu = cursemenu(main_menu_items, self.screen)

		main_menu.display()

