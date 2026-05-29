nums = [1, 3, 5, 7, 9]
def show(nums):
    for i in range(0, len(nums)):
        print(nums[i])
#show(nums)
nums.append(11)
#show(nums)
nums.insert(0, -1)
#show(nums)
deleted = nums.pop(0)
#print(deleted)
#show(nums)
if -1 not in nums:
    print('okay')
target = int(input())
if target in nums:
    idx = nums.index(target)
    print(f"Your index {idx}")
else:
    print("No objects found")
my_list = []
while True:
    temp = input()
    if temp == 'stop':
        break
    else:
        my_list.append(int(temp))
