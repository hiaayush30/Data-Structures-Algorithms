letters = ['a','b','c','d','e']

letters_copy = letters
letters_copy[0] = "B"
print(letters)

letters_copy2 = letters[:]
letters_copy2[0] = "YO"
print(letters)

print(letters[::2]) #returns every second element (starts from 1st)
print(letters[::-1])

def shuffle(self, nums, n):
    newNums = []
    index = 0
    x_index = 0
    y_index = n 
    while index <=  n*2 -1:
        if index%2 == 0:
            newNums.append(nums[x_index])
            x_index +=1
        else:
            newNums.append(nums[y_index])
            y_index += 1
        index += 1
    return newNums

def shuffle2(nums, n):
    newNums = []
    list1 = nums[0:n]
    list2 = nums[n:]
 
    for val1,val2 in zip(list1,list2):
        newNums.append(val1)
        newNums.append(val2)
    print(newNums)
shuffle2([10,20,30,40,50,60],3)

        
num = 96699
li=[]
while num > 0:
   li.append(num%10)
   num = int(num/10)
li.reverse()
for i in range(0,len(li)):
    if li[i] == 6:
        li[i] = 9
        break
print(int("".join(map(str,li))))

print("B" in letters)