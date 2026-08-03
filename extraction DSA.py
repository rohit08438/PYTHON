N=int(input("Enter a number: "))
Num=N
count=0
while Num > 0:
    count+=1
    Num//=10
print(count)
    