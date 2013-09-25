import sys
list1 = sys.argv
list1.remove('ex.py')
list1.sort()
n = len(list1)
list1.insert(n-1, 'and')
n = len(list1)
str1 = ', '.join(list1[0:-1])
str1 += ' ' + list1[-1] + '.'
print str1.capitalize()
letters = str('abcdefghijklmnopqrstuvwxyz') 
str1 = str1.lower()
set1 = set(str1).intersection(letters)
print len(set1), set1
