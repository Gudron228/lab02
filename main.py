from Graph import Graph

def readGraph(fileName):
    with open(fileName, 'r') as file:
        n, m = map(int, file.readline().split())
        graph = Graph(n, m)
        for _ in range(m):
            u, v, w = map(int, file.readline().split())
            graph.addEdge(u, v, w)

    return graph

def writeGraph(fileName, minOstovEdges, ostovWeight):
    if minOstovEdges is None:
        print("Ошибка: невозможно записать дерево, так как оно не существует.")
        return
    with open(fileName, 'w') as file:

        file.write("Остовное дерево минимального веса\n")
        for w, u, v in minOstovEdges:
            file.write(f"Ребро: {u} - {v}, вес: {w}\n")
        file.write(f"Общий вес: {ostovWeight}\n")



def main():
    inputFile = 'graph.txt'
    outputFile = 'output.txt'

    G = readGraph(inputFile)
    minOstovEdges, ostovWeight = G.prima()
    writeGraph(outputFile, minOstovEdges, ostovWeight)


if __name__ == "__main__":
    main()

