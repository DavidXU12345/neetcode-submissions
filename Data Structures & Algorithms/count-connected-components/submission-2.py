class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            while parent[n1] != n1:
                parent[n1] = parent[parent[n1]]
                n1 = parent[n1]
            return n1
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        count = n
        for n1, n2 in edges:
            if union(n1, n2):
                count -= 1
        return count
                

