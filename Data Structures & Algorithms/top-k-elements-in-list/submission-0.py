class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary
        numFrequency = {}

        # count how many times each number occurs in the array and track it with the dictionary
        for i in nums:
            if i in numFrequency:
                numFrequency[i] += 1
            else:
                numFrequency[i] = 1

        # create a list of the numbers sorted by their frequency
        sortedNumbers = sorted(numFrequency, key=numFrequency.get, reverse=True)
        

        # return a list of the k most frequnct elements
        numTopK = sortedNumbers[:k]

        return numTopK