class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary.
        numFrequency = {}

        # Count how many times each number occurs in the array and track it with the dictionary.
        for i in nums:
            if i in numFrequency:
                numFrequency[i] += 1
            else:
                numFrequency[i] = 1

        # Create a list of the numbers sorted by their frequency.
        sortedNumbers = sorted(numFrequency, key=numFrequency.get, reverse=True)

        # Return a list of the k most frequent elements.
        numTopK = sortedNumbers[:k]

        return numTopK