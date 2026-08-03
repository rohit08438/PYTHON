n=int(input("Enter a number: "))
nod=len(str(n))
total=0
while n>0:
    ld=n%10
    total=total+(ld**nod)
    n=n//10
print(total)