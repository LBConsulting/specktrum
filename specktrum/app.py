from flask import Flask, render_template

app = Flask(__name__)

app.route("/")
def main():
    """
    takes a GET request of 3 colours and build 4 colours for each
    colours: a,b,c
    variations: +/-20% saturation, +/-20% brightness
    """
    return render_template()

if __name__ == "__main__":
    app.debug = True
    app.run()
