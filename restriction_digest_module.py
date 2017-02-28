#import Bio.SeqIO

def TRYPSIN(sequence):
    cut_sites = [0]
    for i in range(0,len(sequence)-1):
        if sequence[i] == 'K' and sequence[i+1] != 'P':
            cut_sites.append(i+1)
        elif sequence[i] == 'R' and sequence[i+1] != 'P':
            cut_sites.append(i+1)

    if cut_sites[-1] != len(sequence):
        cut_sites.append(len(sequence))
    return cut_sites
    
def missed_cleavage(sequence,miss_cleavage,cut_sites):
    peptides = []
    if len(cut_sites) > 2:
        # No missed cleavage
        if miss_cleavage == 0:
            for j in range(0,len(cut_sites)-1):
                peptides.append(sequence[cut_sites[j]:cut_sites[j+1]])
        # 1 missed cleavage
        elif miss_cleavage == 1:
            for j in range(0,len(cut_sites)-2):
                peptides.append(sequence[cut_sites[j]:cut_sites[j+1]])
                peptides.append(sequence[cut_sites[j]:cut_sites[j+2]])
            peptides.append(sequence[cut_sites[-2]:cut_sites[-1]])

        # 2 missed cleavages
        elif miss_cleavage == 2:
            for j in range(0,len(cut_sites)-3):
                peptides.append(sequence[cut_sites[j]:cut_sites[j+1]])
                peptides.append(sequence[cut_sites[j]:cut_sites[j+2]])
                peptides.append(sequence[cut_sites[j]:cut_sites[j+3]])

            peptides.append(sequence[cut_sites[-3]:cut_sites[-2]])
            peptides.append(sequence[cut_sites[-3]:cut_sites[-1]])
            peptides.append(sequence[cut_sites[-2]:cut_sites[-1]])
    else:
        peptides.append(sequence)
    return peptides
    
def peptide_dictionary(peptides):
    AA_weight = {'A':89,'R':174,'N':132,'D':133,'B':133,'C':121,'Q':146,'E':147,'Z':147,'G':75,'H':155,'I':131,'L':131,'K':146,'M':149,'F':165,'P':115,'S':105,'T':119,'W':204,'Y':181,'V':117}
    peptide_dictionary = {}
    for peptide in peptides:
        peptide_weight = 0
        for letter in peptide:
            peptide_weight = AA_weight[letter] + peptide_weight
        #peptide_weights.append(peptide_weight)
        peptide_dictionary[peptide] = [peptide_weight,len(peptide)]
    return peptide_dictionary

    
def read_seq_from_file(seqfilename):
    sequence = []
    seqfile = open(seqfilename)
    for seq_record in Bio.SeqIO.parse(seqfile,"fasta"):
        sequence.append(seq_record.seq)
    sequence = str(sequence[0])
    seqfile.close()
    return sequence