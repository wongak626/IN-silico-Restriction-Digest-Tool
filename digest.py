from flask import Flask, render_template, request
from forms import InputForm
from restriction_digest_module import *


app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
	form = InputForm()
	return render_template("index.html",form = form)
	
@app.route('/result',methods = ['POST','GET'])
def result():
	if request.method == 'POST':
		sequence_AA = str(request.form['sequence_input'])
		if sequence_AA:
			sequence_AA = sequence_AA.replace('\n','').replace('\r','')
		enzyme = str(request.form['enzyme'])
		missed_cleavage_number = int(request.form['missed_cleavage'])
		min_weight = int(request.form['min_weight'])
		max_weight = int(request.form['max_weight'])
		min_length = int(request.form['min_length'])
		max_length = int(request.form['max_length'])
		
		input = digest(sequence_AA, missed_cleavage_number,min_weight, max_weight, min_length, max_length)
		# check specific enzyme and create cut sites
		if enzyme == "Trypsin":
			result = input.peptide_filter(input.peptide_dictionary(input.missed_cleavage(input.TRYPSIN())))
		elif enzyme == "CNBr":
			result = input.peptide_filter(input.peptide_dictionary(input.missed_cleavage(input.CNBr())))
		elif enzyme == "Lys C":
			result = input.peptide_filter(input.peptide_dictionary(input.missed_cleavage(input.LYSC())))
				
		
		
		return render_template("results.html", result = result)
	
if __name__ == "__main__":
	app.run()