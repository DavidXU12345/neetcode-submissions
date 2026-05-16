class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_s = sorted(s)
            anagrams[str(sorted_s)].append(s)
        result = []
        for anagram_list in anagrams.values():
            result.append(anagram_list)
        return result