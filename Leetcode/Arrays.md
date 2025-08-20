## Contains Duplicate
```
Dictionary lookups and insertions take, on average, constant time, O(1).
```
- optimized
```python
class Solution(object):
    def containsDuplicate(self, nums):
        myset = set()
        for i in range(0,len(nums)):
          if nums[i] in myset:
            return True
          else:
            myset.add(nums[i])
        return False
```
- even better
```python
class Solution(object):
    def containsDuplicate(self, nums):
        d={}
        
        for i in nums:
            if i in d:
                return True
            if i not in d:
                d[i]=1
        return False  
```

## Check if Anagram
```python
def isAnagram(s,t):
    return sorted(s) == sorted(t)
```
```python
def isAnagram(s, t):
        if not len(s) == len(t):
            return False
        
        mapping =  {}
        for char in s:
            mapping[char] = mapping.get(char, 0) + 1
        for char in t:  
            if mapping.get(char,0) == 0:
                return False
            else:
                mapping[char] -= 1

        return True


print(isAnagram("cta","cat"))
```

## 2 Sum
- brute force
```python
# O(n^2) time
# O(1) space
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
```
- optimized
```python
>> O(n) time complexity
>> It only requires a single pass through the list.
>> O(n) space complexity
>> In the worst-case scenario, the dictionary might store all n elements if no pair sums to the target.
```
```python
def twoSum(self, nums, target):
        seen = {}
         # will have numbers and their indexes
        for index,val in enumerate(nums):
            compliment = target - val
            if compliment in seen:
                return [seen[compliment],index]
            else:
                seen[val] = index
```

## Longest COmmon Prefix
- O (m*n) time complexity
```python
def LongestCommonPrefix(arr):
    prefix = ""
    
    for i in range(len(arr[0])):
        for word in arr:
            if arr[0][i] != word[i] or i == len(word):
                return prefix
        prefix += arr[0][i] 


print(LongestCommonPrefix(arr))
```