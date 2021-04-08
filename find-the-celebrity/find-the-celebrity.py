# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        celebrity = 0
        for person in range(1,n):
            if knows(celebrity, person):
                celebrity = person
        
        for person in range(n):
            if person == celebrity:
                continue
            if (not knows(person, celebrity) or knows(celebrity, person)):
                return -1
            
        return celebrity
        