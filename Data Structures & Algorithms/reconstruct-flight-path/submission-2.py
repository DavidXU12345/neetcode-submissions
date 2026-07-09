class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        for src, dest in tickets:
            adj[src].append(dest)
        res = []
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop()
                dfs(dest)
            # only append if it is a deadend, so no need to be backtracked, only go through all edges once
            res.append(src)
        
        dfs("JFK")
        return res[::-1]