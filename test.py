from func import nucleotideContent
test = [['gtcagtc',{'G':2,'T':2,'C':2,'A':1}],['actGHR',{}],['gtagt',{'G':2,'T':2,'A':1}]]

passes = 0    
for (i, [seq, expected]) in enumerate(test):
    if nucleotideContent(seq) == expected:    
        passes += 1    
    else:    
        print('test %d failed' % i)    
print('%d/%d tests passed' % (passes, len(test)))

