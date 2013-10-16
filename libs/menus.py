# -*- coding: utf-8 -*-
from libs.cursesctrl import cursemenu, endcrs
import aptgets

none = ""

def display():
	try:
		aptupd = aptgets.startApt('1')

		aptitude_items = [
				("Update apt lists", aptupd)
				]
		aptmenu = cursemenu(aptitude_items)

		gitmenu_items = [
				("pull known git repos(Unimprement)", none)
				]
		gitmenu = cursemenu(gitmenu_items)

		main_menu_items = [
				("Manage aptitude", aptmenu.display),
				("Manage cloned gits", gitmenu.display)
				]
		main_menu = cursemenu(main_menu_items)

		main_menu.display()

# Dirtayyyy lets just bounce out.
	except Exception, e:
		endcrs()
		print "Something went wrong. %s" % e