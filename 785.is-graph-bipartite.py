#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#THIOR GREAPH

# @lc code=start

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colour = [-1]*len(graph)
        visit = set()
        
        #idea of graph colouring using bfs
        def bfs(graph,colour,source):
            q = deque([source])
            colour[source] = 1
            while q:
                curr = q.popleft()
                visit.add(curr)
                for neighbour in graph[curr]:
                    if colour[neighbour] == colour[curr]:
                        return False
                    if colour[neighbour] == -1:
                        colour[neighbour] = 1-colour[curr]
                        q.append(neighbour)
            return True
        
        #as there are different connected components
        for v in range(len(graph)):
            if v not in visit:
                bipartite_check = bfs(graph,colour,v)
                if bipartite_check == False:
                    return False
        return True
        
# @lc code=end

