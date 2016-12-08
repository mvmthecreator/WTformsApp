from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, BooleanField, HiddenField, FormField



app = Flask(__name__)
app.secret_key = "bcjpkdasfirueijfimfpwke"


class GuestForm(FlaskForm):
    id = HiddenField()
    email = StringField('Email')
    age = StringField('Age')
    vip = BooleanField()



class MainForm(FlaskForm):
    name = StringField('Name')
    guests = FieldList(FormField(GuestForm), min_entries=3)



@app.route('/')
def index():
    form = MainForm()
    return render_template('index.html', form=form)



if  __name__ == '__main__':
    app.run(debug=True, port=5005)