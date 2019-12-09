#!/usr/bin/env python



class Solution:
    def flipgame(self, fronts, backs):
        n = len(fronts)
        d_list = {}
        for i in range(n):
            if fronts[i] in d_list:
                d_list[fronts[i]].append(backs[i])
            else:
                d_list[fronts[i]] = [backs[i]]
            if backs[i] in d_list:
                d_list[backs[i]].append(fronts[i])
            else:
                d_list[backs[i]] = [fronts[i]]


        all_list = fronts + backs
        all_list.sort()

        for number in all_list:
            if number not in d_list[number]:
                return number
        return 0



sol = Solution()
print(sol.flipgame([1,2,4,4,7] ,[1,3,4,1,3]))

