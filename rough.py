arr=["cat","cab","can"]

def LongestCommonPrefix(arr):
    prefix = ""
    
    for i in range(len(arr[0])):
        for word in arr:
            if arr[0][i] != word[i] or i == len(word):
                return prefix
        prefix += arr[0][i] 


print(LongestCommonPrefix(arr))

def majorityElement(nums):
        
        mydict={}
        
        for num in nums:
            mydict[num] = mydict.get(num,0)+1
        
        max = 0
        for val in list(mydict):
        #     if mydict[key] > max:
        #         max = key
        # return max
           print(val)

print(majorityElement([1,1,2,3,3,3,3,3]))