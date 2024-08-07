def twoSum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return [-1, -1] #shouldn't be here

    #this has less than O(n^2) time complexity. or does it?!
    soFar = []
    for i, num in enumerate(nums):
        if target - num in soFar:
            return [soFar.index(target - num), i]
        else:
            soFar.append(num)
    return [-1, -1] #shouldn't be here


# Example 1:
# Input: 
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: 
nums = [3,2,4]
target = 6
print(twoSum(nums, target))
# Output: [1,2]

# Example 3:
# Input:
nums = [3,3]
target = 6
print(twoSum(nums, target))
# Output: [0,1]
 
