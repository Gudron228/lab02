import heapq


class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.L = n // 10
        self.adjacencyList = {i: [] for i in range(1, n + 1)}

    def addEdge(self, u, v, w):
        self.adjacencyList[u].append((v, w))
        self.adjacencyList[v].append((u, w))

    def isValidTree(self, minOstovEdges):
        degrees = {i: 0 for i in range(1, self.n + 1)}

        for u, v, _ in minOstovEdges:
            degrees[u] += 1
            degrees[v] += 1

        leafCount = 0
        for degree in degrees.values():
            if degree == 1:
                leafCount += 1

        print(f"Степени вершин остовного дерева: {degrees}")
        print(f"Количество листьев: {leafCount}")

        for degree in degrees.values():
            if degree > 3:
                print(f"Ошибка(Неправильная степень: {degree})")
                return False

        if leafCount > self.L:
            print(f"Ошибка(Слишком много листьев: {leafCount})")
            return False

        return True

    def prima(self):
        minOstovEdges = []
        visited = set()
        ostovWeight = 0
        minHeap = []

        startVertex = 1
        visited.add(startVertex)
        for neighbor, weight in self.adjacencyList[startVertex]:
            heapq.heappush(minHeap, (weight, startVertex, neighbor))

        while minHeap and len(visited) < self.n:
            w, u, v = heapq.heappop(minHeap)

            if v not in visited:
                visited.add(v)
                minOstovEdges.append((u, v, w))
                ostovWeight += w

                for neighbor, weight in self.adjacencyList[v]:
                    if neighbor not in visited:
                        heapq.heappush(minHeap, (weight, v, neighbor))


        if len(minOstovEdges) != self.n - 1:
            print("Граф не связан")
            return None, None

        if not self.isValidTree(minOstovEdges):
            print("Ошибка при проверке дерева с ограничениями")
            return None, None

        return minOstovEdges, ostovWeight


    def __str__(self):
        result = []
        for vertex, edge in self.adjacencyList.items():
            result.append(f"{vertex}: {edge}")
        return "\n".join(result)



