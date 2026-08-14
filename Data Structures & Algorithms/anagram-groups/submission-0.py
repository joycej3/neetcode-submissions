class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            hm = {}
            for c in s:
                hm[c] = 1 + hm.get(c,0)
            key = frozenset(hm.items())
            res[key].append(s)
        return list(res.values())
            