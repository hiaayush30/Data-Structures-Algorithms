def removeDuplicates(nums):
    index = 0
    while index < len(nums) - 1:  # stop before last element
        if nums[index] == nums[index + 1]:
            nums.pop(index + 1)  # remove duplicate element
        else:
            index += 1
    return nums

nums = [10,10,20,20,40]
def removeDuplicates1(nums):
        uniques = sorted(set(nums))   # extra memory + sort
        k = len(uniques)
        nums[:k-1] = uniques            # write back so nums[:k] is correct
        return k

removeDuplicates(nums)
print(nums)


# 2 pointer method
def removeVal(nums,val):
     k = 0
     for i in range(0,len(nums)):
        if nums[i] != val:
         nums[k] = nums[i]
         k +=1
     return k

print(removeVal([1,2,3,1,3,4],1))