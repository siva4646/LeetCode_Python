# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for person in range(1, n):
            if knows(celebrity, person):
                celebrity = person
                
        for person in range(n):
            if person == celebrity:
                continue
            if (not knows(person, celebrity) or knows(celebrity, person)):
                return -1
            
        return celebrity
        