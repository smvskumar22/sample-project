n=int(input("enter a number:"))
temp=n
ams=0
st=str(n)
digits=0
for i in st:
    digits=digits+1
while n>0:
    rem=n%10
    ams=ams+(rem**digits)
    n=n//10
if  temp==ams:
    print("armstrong")
else:
    print("not armstrong")
