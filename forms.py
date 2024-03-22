from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,IntegerField,TextAreaField,BooleanField
from wtforms.validators import InputRequired, URL,Optional, NumberRange,Length

class AddPetForm(FlaskForm):
    name=StringField('Pet Name',validators=[InputRequired()])
    species=SelectField('Pet Species',choices=[('dog','dog'),('cat','cat'),('porcupine','porcupine')])
    photo_url=StringField('Pet Photo URL',validators=[URL(),Optional()])
    age=IntegerField('Age', validators=[Optional(), NumberRange(min=0,max=30)])
    notes=TextAreaField("Comments",validators=[Optional(),Length(min=10)])

class EditPetForm(FlaskForm):
    photo_url=StringField('Pet Photo URL',validators=[URL(),Optional()])
    notes=TextAreaField("Comments",validators=[Optional(),Length(min=10)])
    available=BooleanField('Available?')
