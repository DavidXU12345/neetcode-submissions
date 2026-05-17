class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            anagram_dict[''.join(sorted(s))].append(s)
        res = []
        for _, v in anagram_dict.items():
            res.append(v)
        return res