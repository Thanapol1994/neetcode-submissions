class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare dictionary
        result = dict()

        # traverse the strs
        for i in strs:
            #check if the sorted word matches to one of keys in the dictionary
            sortedWord = ''.join(sorted(i))
            if sortedWord in result:
                # if match, add the original word to the sorted key
                result[sortedWord].append(i)
                # if not match, add the sorted as a new key in the dictionary and its original word as a value.
            else:
                result[sortedWord] = [i]
        return list(result.values())