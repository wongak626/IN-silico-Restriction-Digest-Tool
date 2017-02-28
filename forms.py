from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, SelectField, IntegerField

class InputForm(Form):
	sequence_input = TextAreaField("Input AA Sequence")
	submit = SubmitField("Perform Cleavage")
	enzyme = SelectField('Restriction Digest', choices = [('Trypsin','Trypsin')])
	missed_cleavage = SelectField('Number of missed cleavages', choices = [(0,0),(1,1),(2,2)])
	min_weight = IntegerField("Minimum Weight")
	max_weight = IntegerField("Maximum Weight")
	min_length = IntegerField("Minimum Length")
	max_length = IntegerField("Maximum Length")
	