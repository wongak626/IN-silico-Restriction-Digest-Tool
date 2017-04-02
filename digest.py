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
		enzyme = str(request.form['enzyme'])
		missed_cleavage_number = int(request.form['missed_cleavage'])
		# check specific enzyme and create cut sites
		if enzyme == "Trypsin":
			cut_sites = TRYPSIN(sequence_AA)
			peptides = missed_cleavage(sequence_AA, missed_cleavage_number,cut_sites)
		elif enzyme == "CNBr":
			cut_sites = CNBR(sequence_AA)
			peptides = missed_cleavage(sequence_AA, missed_cleavage_number,cut_sites)
		elif enzyme == "Lys C":
			cut_sites = LYSC(sequence_AA)
			peptides = missed_cleavage(sequence_AA, missed_cleavage_number,cut_sites)
				
		
		peptide_dict = peptide_dictionary(peptides)
		min_weight = int(request.form['min_weight'])
		max_weight = int(request.form['max_weight'])
		min_length = int(request.form['min_length'])
		max_length = int(request.form['max_length'])
		result = {}
		for peptide, (peptide_weight,peptide_length) in peptide_dict.iteritems():
			peptide_weight = float(peptide_weight)
			peptide_length = float(peptide_length)
			if min_weight <= peptide_weight <= max_weight:
				if min_length <= peptide_length <= max_length:
					result[peptide] = [peptide_weight, peptide_length]
		
		return render_template("results.html", result = result)
	
if __name__ == "__main__":
	app.run()