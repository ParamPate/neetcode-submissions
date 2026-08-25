class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sig = "".join(sorted(word))
            if sig not in seen:
                seen[sig] = [word]
            else:
                seen[sig].append(word)
        return list(seen.values())
        
