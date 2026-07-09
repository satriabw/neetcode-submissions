class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort the string, put it as a key to map
        # Then the has map is grouping of the array
        # String length is <= 100 so it is reasonabke

        results = []
        anagram = {}

        for string in strs:
            key = ''.join(sorted(string))
            anagram.setdefault(key, [])
            anagram[key].append(string)
        
        for _, val in anagram.items():
            results.append(val)
        
        return results
