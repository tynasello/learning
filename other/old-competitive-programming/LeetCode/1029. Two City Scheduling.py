class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        res = 0

        citiesOccupied = [0, 0]
        differences = []

        for i, cost in enumerate(costs):
            differences.append([abs(cost[0]-cost[1]), i])

        differences.sort()

        for i in range(2 * n - 1, -1, -1):
            cost = costs[differences[i][1]]
            if (citiesOccupied[0] == n):
                res += cost[1]
                citiesOccupied[1] += 1
            elif (citiesOccupied[1] == n):
                res += cost[0]
                citiesOccupied[0] += 1
            else:
                if (cost[0] < cost[1]):
                    res += cost[0]
                    citiesOccupied[0] += 1
                else:
                    res += cost[1]
                    citiesOccupied[1] += 1

        return res
