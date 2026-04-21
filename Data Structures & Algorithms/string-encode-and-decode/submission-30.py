class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        
        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        if not s:
            return res
        
        i = 0
        while i < len(s):
            length = ""
            for n in range(len(s)):
                length += s[i]
                i += 1
                if s[i] == "#":
                    break

            length = int(length)
            res.append(s[i + 1 : i + length + 1])
            i += length + 1

        return res