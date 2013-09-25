str1 = 'ATCGGGGGGCGGGCGGGTTTTTCCCCCCCCCCAAAAAAAAAAA'
str1 = str1.upper()
dict1 = {'A':str1.count('A'), 'C':str1.count('C'), 'G':str1.count('G'), 'T':str1.count('T')}
print dict1

print (dict1['C']+dict1['G'])/float(len(str1))



