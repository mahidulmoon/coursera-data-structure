name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=0
lst=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '): continue
    words=line.split()
    time=words[5]
    hr=time.split(':')
    flag=hr[0]
    lst[flag]=lst.get(flag,0)+1

list2=list()
for value,count in lst.items():
    list2.append((value,count))

list1=sorted(list2)
for value,count in list1:
    print (value,count)