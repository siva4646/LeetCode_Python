class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b =="0":
            return "0"
        binary_sum = int(a,2) + int(b, 2)
        final_res = bin(binary_sum)
        return final_res.lstrip("0b")
        