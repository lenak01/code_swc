def gc_content(dna):
    #if dna.isalpha():????????????????????????
	str1 = dna.upper().replace('N','')
	return (str1.count('C')+str1.count('G'))/float(len(str1))
    #else:
	#return 'usage'

def fasta_stats(filename):
    reader = open(filename,'r')
    line = reader.readline()
    ave = 0
    i = 0
    while line != '':
        if line.startswith('>'):
            print line[1:].rstrip()
            i += 1
        else:
        	str1 = line.rstrip().upper().replace('N','')
	        print 'N: ', line.count('N'), ' GC: ', (str1.count('C')+str1.count('G'))/float(len(str1))
        line = reader.readline()
    reader.close()
    print 'total: ', i, ' lines'


fasta_stats('ex.fasta')
#print gc_content('ATCGGGGGGCGGGCGGGTTTTTCCCCCCCCCCAAAAAAAAAAA')

def dna_starts(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    return (str1.startswith(str2))

print dna_starts('ATGGGGGTGTGTGNNNNNNTGA', 'atg')

def nucleotideContent(dnaString):    
    '''This function must return the contribution of nucleotides ATCG (as uppercase) from a given
    DNA string inside a dictionary, where each key refers to a nucleotide'''    
    dnaDict = {}
    dnaStr = dnaString.upper()  
    uniques=set(dnaStr)    
    for nucleotide in uniques:    
        dnaDict[nucleotide]=dnaStr.count(nucleotide)    
    return dnaDict

