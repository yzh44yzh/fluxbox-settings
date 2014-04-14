#! /usr/bin/python
# -*- coding: utf-8 -*

import pygtk, gtk
pygtk.require("2.0")
import subprocess, gobject

icon = gtk.StatusIcon()
#icon = gtk.status_icon_new_from_file('icons/4/battery_missing.png')

def update():
    global icon
    p = subprocess.Popen("acpi -b", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    # Battery 0: Discharging, 43%, 01:56:34 remaining\n
    percent_str = output.split(", ")[1].split("%")[0]
    percent = (int(percent_str) / 5) * 5

    icon.set_from_file("icon/%s.png" % percent)
    icon.set_tooltip(output)
    gobject.timeout_add_seconds(5, update)

update()

gtk.main()
