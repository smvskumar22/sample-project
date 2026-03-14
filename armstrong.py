n1=int(input("enter a number:"))
temp=n1
ams=0
st=str(n1)
digits=0
for i in st:
    digits=digits+1
while n>0:
    rem=n%10
    ams=ams+(rem**digits)
    n1=n1//10
if  temp==ams:
    print("armstrong")
else:
    print("not armstrong")
