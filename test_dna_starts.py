def dna_starts_with(st1, st2):
    return st1[0:len(st2)]==st2
    
def test_dna_starts_with_itself():
    dna='acgtgtcgat'
    assert dna_starts_with(dna, dna)
    
def test_dna_starts_with_one():
    assert dna_starts_with('cgtgc', 'c')
    
def test_dna_starts_with_bigger():
    dna='acgtgtcgat'
    assert not dna_starts_with(dna, dna+dna)
    

test_dna_starts_with_itself()
test_dna_starts_with_one()
test_dna_starts_with_bigger()

