__author__ = 'kristoffer'

import webkit
import gtk
import os
import json
import calc

win = gtk.Window()
win.resize(600, 400)
win.connect('destroy', lambda w: gtk.main_quit())

scrollView = gtk.ScrolledWindow()
win.add(scrollView)

web = webkit.WebView()
path = os.getcwd()
print path

web.open("file://" + path + "/index.html")

scrollView.add(web)

def window_title_change(web, param):
    if not web.get_title():
        return
    if web.get_title().startswith("msgToPython:::"):
        message = web.get_title().split(":::",1)[1]
        # Now, send a message back to JavaScript
        print 'h',calc.parseIt(message)
        return_message = "You chose '%s'. How interesting." % calc.parseIt(message)
        web.execute_script("jsCallback(%s)" % json.dumps(calc.parseIt(message)))


web.connect("notify::title", window_title_change)

win.show_all()

gtk.main()