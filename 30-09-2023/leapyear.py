y=int(input("current year:"))
c=int(input("future year:"))
for year in range(y,c):
    if(0==year%4):
        print(year)

        
