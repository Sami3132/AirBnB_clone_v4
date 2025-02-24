class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobPath = dict()
        
        def findBobPath(node, parent, depth):
            if node == 0:
                bobPath[node] = depth
                return True
            for neighbor in graph[node]:
                if neighbor != parent and findBobPath(neighbor, node, depth + 1):
                    bobPath[node] = depth
                    return True
            return False
        
        findBobPath(bob, -1, 0)
        
        def modifyAmount(node, parent, depth):
            if node in bobPath:
                bobDepth = bobPath[node]
                if bobDepth > depth:
                    pass
                elif bobDepth == depth:
                    amount[node] //= 2
                else:
                    amount[node] = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    modifyAmount(neighbor, node, depth + 1)
        
        modifyAmount(0, -1, 0)
        
        def dfs(node, parent):
            if len(graph[node]) == 1 and node != 0:
                return amount[node]
            
            maxProfit = float("-inf")
            for neighbor in graph[node]:
                if neighbor != parent:
                    maxProfit = max(maxProfit, dfs(neighbor, node))
            
            return amount[node] + (maxProfit if maxProfit != float("-inf") else 0)

        return dfs(0, -1)
