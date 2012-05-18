from flask import Flask, render_template, request
from forms import ColorSelectionForm
from utils import pagefromcolors

app = Flask(__name__)

# the main show
@app.route("/", methods=['GET', 'POST'])
def main():
    """
    takes a GET request of 3 colours and build 4 colours for each
    colours: a,b,c
    variations: +/-20% saturation, +/-20% brightness
    """
    page = dict()
    form = ColorSelectionForm(request.form)
    if form.validate_on_submit():
        colors = dict(a=form.color_a.data,
                        b=form.color_b.data,
                        c=form.color_c.data)
        page = pagefromcolors(colors)
    return render_template('index.html', page=page, form=form)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "45OIUKX97H8Uu12oiayhtiaet"
    app.run()
