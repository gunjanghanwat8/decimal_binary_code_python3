n=int(input("enter the decimal number"))
b=[]
while (n!=0):
    a=n//2
    b.append(n%2)
    n=a
b=b[::-1]
s=""
for i in b:
    s=s+str(i)
print(int(s))

