class DNA:
    base_complement = {'G': 'C', 'C':'G', 'A': 'T', 'T': 'A'}
    def __init__(self, dna):
        self.dna = dna
        self.length = len(dna)
        self.bases = {}
    def base_count(self, base):
        '''Count the number of times the specified base occures in the sequence'''
        if base not in self.bases:
            self.bases[base] = self.dna.count(base)
        return self.bases[base]
    def cg_content(self):
        return (self.base_count('C')+self.base_count('G'))/float(self.length)
    def rc(self):
        complement = ''
        for base in self.dna:
            complement = self.base_complement[base] + complement
        return complement

