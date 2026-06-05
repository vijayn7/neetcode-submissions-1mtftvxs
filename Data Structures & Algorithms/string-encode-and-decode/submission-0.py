class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            end = i

            while s[end] != '#':
                end += 1

            length = int(s[i:end])

            word = s[end + 1:end + 1 + length]
            res.append(word)

            i = end + 1 + length

        return res