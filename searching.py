target = 112
arr = [112,56,32,48,55]

def linearSearch(target:int,arr):
    for i in range(0,len(arr)):
      if arr[i] == target:
        return i
    return -1

print(linearSearch(target,arr))


def binarySearch(target:int,arr):
   arr.sort()
   start=0
   end = len(arr)-1
   while start<=end:
      middle = int((start+end)/2)
      if arr[middle] == target:
         return middle
      elif arr[middle]>target:
         end = middle-1
      else:
         start = middle+1
   return -1

print(arr)
print(binarySearch(target,arr))