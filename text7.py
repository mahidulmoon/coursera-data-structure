name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=0
store=dict()
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '): continue
    word=line.split()
    flag=word[1]
    store[flag]=store.get(flag,0)+1

mx=0
name=0
for key,value in store.items():
    if value>mx:
        mx=value
        name=key
        
print(name,mx)