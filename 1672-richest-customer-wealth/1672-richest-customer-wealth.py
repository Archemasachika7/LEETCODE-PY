class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        listo = []
        sumo = 0
        for i in range (n):
            sumo = sum(accounts[i])
            listo.append(sumo)
        return max(listo)    