
n=[5,3,2,2,1,5,5,7,5,10]
m=[1,2,3,4,5,6,7,8,9,10]

hash_list=[0]*len(n)
for num in n:
    hash_list[num-1]+=1
for num in m:
    if num<1 or num>len(n):
        print(0)
    else:
        print(hash_list[num-1])

    