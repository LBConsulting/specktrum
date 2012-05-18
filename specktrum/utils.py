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
    with open("static/css/style_template.sass", "r") as f:
        style_tmpl = f.read()
    sassed = style_tmpl % colors
    with open("static/css/style.sass", "w") as f:
        f.write(sassed)
    ##subprocess.call("sass static/css/style.sass > static/css/style.css", shell=True)
    # TODO: make this fully python
    ##ret = subprocess.call(["./sassy.sh", "style"], shell=True)
    ret = subprocess.call(["./sassy.sh"], shell=True)
    if ret == 0:
        return True
    else:
        return False, ret
