a = int(input( "enter your value \n"))
b=int(a)
sum1=0
for i in range(0,b+1):
    if (i%2==0):
        sum=i*i
        sum1=sum1+sum

print("\nAnswer is here ")
print(sum1)