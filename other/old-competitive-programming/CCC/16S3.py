class Node:
    def __init__(self, iVal, isPhoVal):
        self.i = iVal
        self.isPho = isPhoVal
        self.connectedTo = []

    def printi(self):
        print(self.i, self.isPho, self.connectedTo)


def createGraph(numRestaurants, phos):
    nodes = []
    phoRestaurants = []
    for i in range(numRestaurants):
        if i in phos:
            node = Node(i, True)
            phoRestaurants.append(node)
        else:
            node = Node(i, False)
        nodes.append(node)
    return (nodes, phoRestaurants)


def addConection(nodes, id1, id2):
    nodes[id1].connectedTo.append(id2)
    nodes[id2].connectedTo.append(id1)


def dfs(nodes, currNode, visited, farthestNode, maxD, d, listPhos):
    visited[currNode] = 1
    if d > maxD and currNode in listPhos:
        maxD = d
        farthestNode = nodes[currNode]
    for node in nodes[currNode].connectedTo:
        if visited[node] == 0:
            farthestNode, maxD = dfs(
                nodes, node, visited, farthestNode, maxD, d + 1, listPhos
            )
    return farthestNode, maxD


def phoInSubtree(nodes, startingNode, prevNode, containsSubPho):
    if startingNode.isPho:
        containsSubPho[startingNode.i] = True
    for child in startingNode.connectedTo:
        child = nodes[child]
        if child != prevNode:
            containsSubPho = phoInSubtree(nodes, child, startingNode, containsSubPho)
            if containsSubPho[child.i]:
                containsSubPho[startingNode.i] = True
    return containsSubPho


def findCost(nodes, startingNode, prevNode, cost, containsSubPho):
    for child in startingNode.connectedTo:
        if nodes[child] != prevNode:
            if containsSubPho[child]:
                cost = findCost(
                    nodes, nodes[child], startingNode, cost + 2, containsSubPho
                )
    return cost


if __name__ == "__main__":
    numRestaurants, numPhos = map(int, input().split())
    listPhos = list(map(int, input().split()))
    roads = []
    nodes, phos = createGraph(numRestaurants, listPhos)
    for i in range(numRestaurants - 1):
        roads.append(list(map(int, input().split())))
        addConection(nodes, roads[-1][0], roads[-1][1])
    # Pick any pho restaurant and find the pho restaurant which is the farthers distance from it
    # this is our starting point

    visited = [0] * (numRestaurants)
    startingNode, maxDistance = dfs(nodes, phos[0].i, visited, None, 0, 0, listPhos)
    visited = [0] * (numRestaurants)
    startingNode, maxDistance = dfs(
        nodes, startingNode.i, visited, None, 0, 0, listPhos
    )

    containsSubPho = [False] * numRestaurants
    containsSubPho = phoInSubtree(nodes, startingNode, startingNode, containsSubPho)
    cost = findCost(nodes, startingNode, startingNode, 0, containsSubPho)
    ans = cost - maxDistance
    print(ans)