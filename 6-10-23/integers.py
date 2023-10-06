
a=int(input("enter the limit:"))
q=[]
v="over"
for i in range(0,a):
    list=int(input("enter elements:"))
    if list<99:
        q.append(list)
    else:
        q.append(v)
print(q)
