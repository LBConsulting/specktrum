import random
from flask import Flask, render_template, request
from forms import ColorSelectionForm
from utils import pagefromcolors

app = Flask(__name__)
# example colours
baseex = ("993300", "990019", "997f00")

# the main show
@app.route("/", methods=['GET', 'POST'])
def main(rando=None):
    """
    takes a GET request of 3 colours and build 4 colours for each
    colours: a,b,c
    variations: +/-20% saturation, +/-20% brightness
    """
    ## HACK: get a random value for ensuring no css caching
    ## Is it a hack? Now I'm going to use this number to generate hex for
    ## the 'lucky' button.
    # 255*255*255 is based on max hex for rgb color.
    randf = lambda: random.randint(0, 255*255*255)
    randhex = lambda: "%06x" % (random.random() * 0xffffff)
    randcolor = (randhex(), 
                randhex(),
                randhex())
    randn = randf() # ensures css caching
    form = ColorSelectionForm(request.form)
    isrando = request.args.get('rando','')
    if form.validate_on_submit():
        colors = dict(a=form.color_a.data[1:],
                    b=form.color_b.data[1:],
                    c=form.color_c.data[1:])
        page = pagefromcolors(colors)
    elif isrando == "y":
        colors = dict(a=randcolor[0],b=randcolor[1],c=randcolor[2])
        page = pagefromcolors(colors)
        form.color_a.data = "#" + randcolor[0]
        form.color_b.data = "#" + randcolor[1]
        form.color_c.data = "#" + randcolor[2]
    else:
        page = dict(A=dict(base=baseex[0]),
                    B=dict(base=baseex[1]),
                    C=dict(base=baseex[2]))

    return render_template('index.html', page=page, form=form, rando=randn,
            randcolor=randcolor)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "45OIUKX97H8Uu12oiayhtiaet"
    app.run(port=5015)
