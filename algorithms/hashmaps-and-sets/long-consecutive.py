# Given an unsorted array of integers nums, return the 
# length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
# (Consecutive means numbers that follow each other without 
# gaps, e.g., 1,2,3,4. Order in the array does not matter.)

# example:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4]. 
# Its length is 4.

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Constraints

#     0 <= nums.length <= 10^5

#     -10^9 <= nums[i] <= 10^9


Input = dict[str, list[int]]

input: Input = {
    "nums": [100, 4, 200, 1, 3, 2]
}


def findLongestConsec(input: Input):
    # define the set to search for first numbers of sequences
    numsSet = set(input["nums"])
    # define current streak for comparison
    currentStreak = 0
    # define longest streak length
    longestStreak = 0

    # iterate the nums array
    for num in input["nums"]:
        # if there is no sequence number smaller, define current num to find sequence
        if(num - 1 not in numsSet):
            currentNum = num
            # while num is in numsSet, loop to add 1 in sequence
            while currentNum in numsSet:
                currentStreak += 1
                currentNum += 1
            
            # reset streak and find max between currentStreak to longestStreak
            currentStreak = 0
            longestStreak = max(currentStreak, longestStreak)
        
        return longestStreak