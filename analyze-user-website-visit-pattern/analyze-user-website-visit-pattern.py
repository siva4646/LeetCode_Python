class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        userVisit = collections.defaultdict(list)
        for time, user, web in sorted(zip(timestamp, username, website)):
            userVisit[user].append(web)
        
        count = {}
        for x in userVisit.values():
            combination_set = set(combinations(x,3))
            for combination in combination_set:
                if combination not in count:
                    count[combination] = 1
                else:
                    count[combination] += 1
        
        sort_combin = sorted(count.items(), key = lambda x:(-x[1], x[0]))
        return sort_combin[0][0]
                    
                
            
        
        