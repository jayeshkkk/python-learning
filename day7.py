'''
floor division operation (//) is used to print the greatest 
integer of the answer of the devision 




for exponent operation we use (**) operator in python
'''
print(5**12)

#making a simple calcul;ator in python
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=input("enter the operation you want to perform")
if c=="+":
    print(a+b)  
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="//":
    print(a//b)
elif c=="**":
    print(a**b)
