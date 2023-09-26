def primeornot():
    num=int(input("Enter your number"))
    for i in range(2,num):
        if num%i==0:
            print("Not prime")
        elif num==1:
            print("Number is 1")
        else:
            print("Prime")
def evenorodd():
    num=int(input("Enter your number"))
    if num%2==0:
        print("Even")
    elif num==0:
        print("Number is 0")
    else:
        print("Odd")
def posorneg():
    num=int(input("Enter the number"))
    if num>0:
        print("Postive")
    elif num==0:
        print("Number is 0")
    else:
        print("Negative")
def armstrongornot():
    num=int(input("Enter a number: "))
    s=0
    t=num
    while t > 0:
        digit=t % 10
        s+=digit ** 3
        t=t//10
    if num==s:
        print(num,"is armstrong")
    else:
        print(num,"is not armstrong")
def palornot():
    num=int(input("Enter number:"))
    t=num
    s=0
    while t>0:
        d=num%10
        r=(r*10)+d
        t=t//10
    if num==r:
        print("The number is a palindrome")
    else:
        print("The number isn't a palindrome")
while True:
    ch=int(input("Enter your choice"))
    if ch==1:
        primeornot()
    elif ch==2:
        evenorodd()
    elif ch==3:
        posorneg()
    elif ch==4:
        armstrongornot()
    elif ch==5:
        palornot()
    else:
        print("Enter valid choice")
