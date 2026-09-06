class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash map with a dictionary to store value and its index
        hashMap = {} # value : index

        # iterate through the array using index i and compute the complement of the current element.
        for i, val in enumerate(nums):
            diff = target - val
            # check if the complement exist in the hash map
            if  diff in hashMap:
                return [hashMap[diff],i]

            hashMap[val] = i
        
        # if no pair is found, return an empty array
        return
        