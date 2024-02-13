import sys
from queue import PriorityQueue


class Node:
    def __init__(self, node):
        self.id = node
        self.connections = []

    # cost = time, weight = cm it wears down
    def add_connection(self, connection, cost, weight):
        self.connections.append([connection, cost, weight])


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.newNode = Node(node)
        self.nodes[node] = self.newNode

    def add_edge(self, a, b, cost, weight):
        self.nodes[a].add_connection(self.nodes[b], cost, weight)
        self.nodes[b].add_connection(self.nodes[a], cost, weight)


def createGraph(numRoutes):
    graph = Graph()
    for _ in range(numRoutes):
        route = list(map(int, input().split()))
        a = route[0]
        b = route[1]
        cost = route[2]
        weight = route[3]
        if a not in graph.nodes:
            graph.add_node(a)
        if b not in graph.nodes:
            graph.add_node(b)

        graph.add_edge(a, b, cost, weight)
    return graph


def Dijkstras(graph, n, a, t):
    visited = [0] * (n + 1)
    dist = [10000 * (10 ** 5)] * (n + 1)
    dist[a] = 0
    pq = PriorityQueue()
    pq.put((0, a, 0))
    while not pq.empty():
        minDist, i, currSize = pq.get()
        visited[i] = 1
        for neighbourInfo in graph.nodes[i].connections:
            neighbour = neighbourInfo[0]
            cost = neighbourInfo[1]
            weight = neighbourInfo[2]
            if visited[neighbour.id] == 1:
                continue
            distance = dist[i] + cost
            lostWeight = currSize + weight
            if distance < dist[neighbour.id] and lostWeight < t:
                dist[neighbour.id] = distance
                pq.put((distance, neighbour.id, lostWeight))
    return dist


if __name__ == "__main__":
    t, n, r = map(int, input().split())
    graph = createGraph(r)
    a, b = map(int, input().split())

    dist = Dijkstras(graph, n, a, t)
    res = dist[b]
    if res == 10000 * (10 ** 5):
        print(-1)
    else:
        print(res)
