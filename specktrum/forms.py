from wtforms import Field
from flaskext.wtf import Form, BooleanField, TextField, validators,\
PasswordField, FileField, TextAreaField, DateTimeField, RecaptchaField,\
HiddenField, DateField

from flaskext.babel import gettext as _

class ColorSelectionForm(Form):
    color_a = TextField(_("Colour A"), [validators.length(min=7, max=7)])
    color_b = TextField(_("Colour B"), [validators.length(min=7, max=7)])
    color_c = TextField(_("Colour C"), [validators.length(min=7, max=7)])

