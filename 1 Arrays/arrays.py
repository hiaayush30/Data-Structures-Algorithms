arr= [1,2,3,4]
# array is stored as a contiguous block of data in RAM
print(arr[0])

# Reading from an array => O(1)
# Arrays are of fixed size
# (in python and js, you don't see this as they use dynamic arrays)


# we can remove a value from array but we can't actually delete that from memory, the block is still there

# writing to a position in an array (at end) => O(1)
# removing a value  => O(1)
# inserting in between or beginning of an array => O(n) as in arrays, the order of values matter

arr.remove(4)
print(arr[3])