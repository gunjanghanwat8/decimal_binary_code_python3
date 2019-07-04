# convert_decimal_to_binary_code_python3
convert the decimal number to binary

following is the program in python3


n=int(input("enter the decimal number"))
b=[]
while (n!=0):
    a=n//2
    b.append(n%2)
    n=a
b=b[::-1]           #reversed the list
s=""
for i in b:         #converted the list to string 
    s=s+str(i)
print(int(s))       #converted string to int



