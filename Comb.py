class Graph:
    def __init__(self, vertex):
        self.graph = []
        self.V = vertex

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # находим лидеров для каждого множества
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        # Соединяем меньшее множество к большему ( по лидерам )
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        ans = 0
        result = []
        i, e = 0, 0
        # сортируем граф по весам
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Т.к. минимальное остовное дерево ( все вершины связаны ) содержит ровно n-1 рёбер, где n кол-во вершин
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            # Проверка на цикличность.
            x = self.search(parent, u)
            y = self.search(parent, v)
            # Если из разных множеств
            if x != y:
                # Кол-ко ребер
                e += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        for u, v, weight in result:
            ans += weight
            print("Edge:", u, v, "-", abs(weight))
        print(abs(ans))


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1, 7)
    g.add_edge(0, 5, 11)
    g.add_edge(5, 1, 19)
    g.add_edge(1, 2, 50)
    g.add_edge(5, 2, 12)
    g.add_edge(5, 4, 20)
    g.add_edge(4, 2, 10)
    g.add_edge(3, 2, 8)
    g.add_edge(4, 3, 9)
    g.kruskal()

# Позволяет найти MST - минимальное остовное дерево

# # lesson one
# matr = [[0,1,0],[1,0,1],[0,1,0]]
# n,m = len(matr),len(matr[0])
# visited = set()
# def dfs(u: int):
#     print(u)
#     visited.add(u)
#     for i in range(n):
#         if matr[u][i] and i not in visited:
#             dfs(i)
# dfs(0)
# print("-------------------")
# # lessone two
#
# def bfs(matr, start: int, visited_nodes=None):
#     queue = []
#     queue.append(start)
#     visited_nodes = set()
#     while queue:
#         node = queue.pop(0)
#         print(node)
#         visited_nodes.add(node)
#         for i in range(len(matr)):
#             if matr[node][i] and (i not in visited_nodes):
#                 queue.append(i)
#
# if __name__ == "__main__":
#     matr = [[0, 1, 1, 0],
#             [0, 0, 0, 1],
#             [0, 0, 1, 0],
#             [0, 0, 0, 0]]
#     bfs(matr,0)
# # # or
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#
#     print(start)
#
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited
#
#
# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}
#
# dfs(graph, '0')

# g.add_edge(0, 1, 8)
# g.add_edge(0, 2, 5)
# g.add_edge(1, 2, 9)
# g.add_edge(1, 3, 11)
# g.add_edge(2, 3, 15)
# g.add_edge(2, 4, 10)
# g.add_edge(3, 4, 7)
