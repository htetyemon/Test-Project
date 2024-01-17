ls=[29,16,38,40,45] #list
data=99
found=True
index=0

while index < len(ls):
    if ls[index]==data:
        found=False
        break
    index  +=1
if not found:
    ls.append(data)
print(ls)        
