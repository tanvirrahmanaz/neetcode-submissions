from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # '#' porjonto giye length ber korbo
            while s[j] != "#":
                j += 1

            # i theke j er ag porjonto number ache
            length = int(s[i:j])

            # actual word start hobe '#' er por theke
            start = j + 1

            # length poriman character nebo
            word = s[start:start + length]

            result.append(word)

            # next encoded word er starting index
            i = start + length

        return result