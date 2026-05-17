class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)
        
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in adj:
                return False
            
            for idx, dest in enumerate(adj[src]):
                adj[src].pop(idx)
                res.append(dest)
                if dfs(dest):
                    return True
                adj[src].insert(idx, dest)
                res.pop()
            return False
        
        dfs("JFK")
        return res