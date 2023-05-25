
a=[20,10,50,50,4,10,12,1,0,1,2,34]
sum=0;

for x in a:
    sum+=x
    print(x)
print("Total = ",sum+a[5],"tk")

b= int(input("Enter the first  number : "))
l= int(input("Enter the last  number : "))
sum=0
for x in  range (b,l+1,1):
    sum=sum+x
print("Total sum is ",sum,"tk")

text = input("Enter the your Numbers")

n=text.split()
sum=0
for x in n:
    sum=sum+int(x)

print(sum)