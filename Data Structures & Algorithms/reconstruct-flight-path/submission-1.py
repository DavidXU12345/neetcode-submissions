class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ['JFK']
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in adj:
                # if it is a deadend, it needs to be backtracked
                return False
            
            temp = list(adj[src])
            for i, dst in enumerate(temp):
                res.append(dst)
                adj[src].pop(i)
                if dfs(dst):
                    return True
                adj[src].insert(i, dst)
                res.pop()
            
            return False

        dfs('JFK')
        return res
