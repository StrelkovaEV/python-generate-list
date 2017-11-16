f = open('workfile.txt', 'r+')
for x in range(999, 100000000):
    f.write(str(x)+'\n')
f.close
