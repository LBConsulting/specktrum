import os
import subprocess

def pagefromcolors(colors):
    page = dict(
            A=dict(base=colors['a']),
            B=dict(base=colors['b']),
            C=dict(base=colors['c'])
        )
    if sassysays(colors) == False:
        print "ERROR"
        return False
    return page

def sassysays(colors):
    '''
    returns a stylesheet rendered by sass
    '''
    style_tmpl = ""
    with open("static/css/style.sass", "r") as f:
        style_tmpl = f.read()
    ##print colors
    ##print style_tmpl
    sassed = style_tmpl % colors
    print "Formatted: \n" + sassed
    with open("static/css/style_set.sass", "w+") as f:
        f.write(sassed)
    ##subprocess.call("sass static/css/style.sass > static/css/style.css", shell=True)
    # TODO: make this fully python
    ##ret = subprocess.call(["./sassy.sh", "style"], shell=True)
    ret = subprocess.call(["./sassy.sh"], shell=True)
    if ret == 0:
        return True
    else:
        return False, ret
