#write a program for armstrong
n=int(input("enter the number"))
sum=0
t=n
while t>0:
    digit=t%10
    sum+=digit**3
    t//=10
    if n==sum :
        print( n,"it is armstrong number")
    else:
        print( n,"it is not armstrong number")
