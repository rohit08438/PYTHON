n=int(input("Enter a number: "))
temp=n
result=0
while n>0:
    ld=n%10
    result=(result*10)+ld
    n=n//10
print(result)
if temp==result:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")