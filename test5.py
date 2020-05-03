fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    line= line.split()
    for c in line:
        if c in lst:
           continue
        else:
           lst.append(c)
            
lst.sort()
print (lst)    