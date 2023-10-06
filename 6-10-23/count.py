n=input("enter the sentence:")
c=input("enter the word to count:")
ls=n.split()
count=0
for n in ls:
    if n==c:
        count=count+1
print("number of",n,"is",count)
