__author__ = 'kristoffer'

import webkit
import gtk
import os
import calc

win = gtk.Window()
win.resize(600, 400)
win.connect('destroy', lambda w: gtk.main_quit())

vBox = gtk.VBox()

toolbar = gtk.Toolbar()
toolbar.set_style(gtk.TOOLBAR_ICONS)

btnTest = gtk.ToolButton(gtk.STOCK_NEW)
toolbar.insert(btnTest,0)


vBox.pack_start(toolbar,False)

scrollView = gtk.ScrolledWindow()
vBox.add(scrollView)
win.add(vBox)

web = webkit.WebView()
path = os.getcwd()
print path

web.open("file://" + path + "/ui/index3.html")

scrollView.add(web)

def window_title_change(web, param):
    if not web.get_title():
        return
    if web.get_title().startswith("msgToPython:::"):
        message = web.get_title().split(":::", 1)[1]
        # Now, send a message back to JavaScript
        list = message.split(',')
        print list
        calc.names={}
        results=""
        for m in list:
            r=calc.parseIt(m)
            results+=calc.sympy.latex(calc.sympy.S(r),mul_symbol='dot').encode('string-escape')+','
        return_message = "You chose '%s'. How interesting." % r
        web.execute_script("jsCallback('%s')" %results)
        print return_message


web.connect("notify::title", window_title_change)

win.show_all()

gtk.main()