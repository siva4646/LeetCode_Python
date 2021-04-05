class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        for query in queries:
            flag = False
            pointer = 0
            for w in query:
                if pointer < len(pattern) and w == pattern[pointer]:
                    pointer += 1
                    if pointer == len(pattern): # FB pointer is next to B here
                        flag = True
                elif w.isupper():
                    flag = False
                    break
            result.append(flag)
        return result
        