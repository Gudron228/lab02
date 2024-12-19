from Graph import Graph
import random

def readGraph(fileName):
    with open(fileName, 'r') as file:
        n, m = map(int, file.readline().split())
        graph = Graph(n, m)
        for _ in range(m):
            u, v, w = map(int, file.readline().split())
            graph.addEdge(u, v, w)

    return graph

def writeGraph(fileName, minOstovEdges, ostovWeight ,g: Graph):
    with open(fileName, 'w') as file:
        file.write("Adjacency List\n")
        file.write(g.adjacencyList.__str__())
        if minOstovEdges is None:
            print("Ошибка: невозможно записать дерево, так как оно не существует.")
            return
        file.write("Minimum weight spanning tree\n")
        for w, u, v in minOstovEdges:
            file.write(f"Edge: {u} - {v}, weight: {w}\n")
        file.write(f"Total weight: {ostovWeight}\n")


def generateRandomGraph(n, m, filename):
    if m > n * (n - 1) // 2:
        raise ValueError("Количество рёбер не может превышать максимальное количество рёбер в простом графе.")

    edges = set()
    while len(edges) < m:
        u = random.randint(1, n)
        v = random.randint(1, n)
        w = random.randint(1, 100)
        if u != v:
            edge = (min(u, v), max(u, v), w)
            if edge[:2] not in {(e[0], e[1]) for e in edges}:
                edges.add(edge)

    with open(filename, 'w') as f:
        f.write(f"{n} {m}\n")
        for u, v, w in edges:
            f.write(f"{u} {v} {w}\n")



def main():
    inputFile = 'graph.txt'
    outputFile = 'output.txt'
    generateRandomGraph(10, 15, inputFile)

    G = readGraph(inputFile)
    print(G)
    minOstovEdges, ostovWeight = G.prima()
    writeGraph(outputFile, minOstovEdges, ostovWeight, G)


if __name__ == "__main__":
    main()

