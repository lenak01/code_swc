reader = open('pg76.txt','r')
line = reader.readline()
n = 0
i = 0
while line != '':
    n += len(line)
    i += 1
    line = reader.readline()
reader.close()
print 'total length: ', n, 'line count: ', i



reader = open('Pitching.csv','r')
line = reader.readline()
line = reader.readline()
ave = 0
i = 0
while line != '':
    ave += float(line.split(',')[12])
    i += 1
    line = reader.readline()
reader.close()
print 'total ipouts: %f, average %f' % (ave, float(ave/i))
