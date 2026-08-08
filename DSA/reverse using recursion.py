def func(nums,l,r):
    if l>=r:
        return
    nums[l],nums[r]=nums[r],nums[l]
    func(nums,l+1 ,r-1)
nums=[1,2,3,4,5]
func(nums,0,4)
print(nums)