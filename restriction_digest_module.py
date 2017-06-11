#import Bio.SeqIO

class digest(object):

	def __init__(self, sequence, miss_cleavage, min_weight, max_weight, min_length, max_length):
		self.sequence = str(sequence)
		self.miss_cleavage = int(miss_cleavage)
#		self.enzyme = str(enzyme)
		self.min_weight = int(min_weight)
		self.max_weight = int(max_weight)
		self.min_length = int(min_length)
		self.max_length = int(max_length)
	
	
	def TRYPSIN(self):
		cut_sites = [0]
		for i in range(0,len(self.sequence)-1):
			if self.sequence[i] == 'K' and self.sequence[i+1] != 'P':
				cut_sites.append(i+1)
			elif self.sequence[i] == 'R' and self.sequence[i+1] != 'P':
				cut_sites.append(i+1)
		
		if cut_sites[-1] != len(self.sequence):
			cut_sites.append(len(self.sequence))
		return cut_sites
	
	def CNBR(self):
		cut_sites = [0]
		for i in range(0,len(self.sequence)-1):
			if self.sequence[i] == 'M':
				cut_sites.append(i+1)
		
		if cut_sites[-1] != len(self.sequence):
			cut_sites.append(len(self.sequence))
		return cut_sites
	
	def LYSC(self):
		cut_sites = [0]
		for i in range(0,len(self.sequence)-1):
			if self.sequence[i] == 'K':
				cut_sites.append(i+1)
		
		if cut_sites[-1] != len(self.sequence):
			cut_sites.append(len(self.sequence))
		return cut_sites
		
		
	def missed_cleavage(self, cut_sites):
		peptides = []
		if len(cut_sites) > 2:
			# No missed cleavage
			if self.miss_cleavage == 0:
				for j in range(0, len(cut_sites)-1):
					peptides.append(self.sequence[cut_sites[j]:cut_sites[j+1]])
			# 1 missed cleavage
			elif self.miss_cleavage == 1:
				for j in range(0,len(cut_sites)-2):
					peptides.append(self.sequence[cut_sites[j]:cut_sites[j+1]])
					peptides.append(self.sequence[cut_sites[j]:cut_sites[j+2]])
				peptides.append(self.sequence[cut_sites[-2]:cut_sites[-1]])
			
			# 2 missed cleavages
			elif self.miss_cleavage == 2:
				for j in range(0,len(cut_sites)-3):
					peptides.append(self.sequence[cut_sites[j]:cut_sites[j+1]])
					peptides.append(self.sequence[cut_sites[j]:cut_sites[j+2]])
					peptides.append(self.sequence[cut_sites[j]:cut_sites[j+3]])
				
				peptides.append(self.sequence[cut_sites[-3]:cut_sites[-2]])
				peptides.append(self.sequence[cut_sites[-3]:cut_sites[-1]])
				peptides.append(self.sequence[cut_sites[-2]:cut_sites[-1]])
		else:
			peptides.append(self.sequence)
		return peptides
	
	def peptide_dictionary(self, peptides):
		AA_weight = {'A':89,'R':174,'N':132,'D':133,'B':133,'C':121,'Q':146,'E':147,'Z':147,'G':75,'H':155,'I':131,'L':131,'K':146, 'M':149, 'F':165, 'P':115, 'S':105,'T':119, 'W':204,'Y':181,'V':117}
		peptide_dictionary = {}
		for peptide in peptides:
			peptide_weight = 0
			for letter in peptide:
				peptide_weight = AA_weight[letter] + peptide_weight
			#peptide_weights.append(peptide_weight)
			peptide_dictionary[peptide] = [peptide_weight, len(peptide)]
		return peptide_dictionary
	
	def peptide_filter(self, peptide_dictionary):
		result = {}
		for peptide, (peptide_weight, peptide_length) in peptide_dictionary.iteritems():
			peptide_weight = float(peptide_weight)
			peptide_length = float(peptide_length)
			if self.min_weight <= peptide_weight <= self.max_weight:
				if self.min_length <= peptide_length <= self.max_length:
					result[peptide] = [peptide_weight, peptide_length]
		return result
	