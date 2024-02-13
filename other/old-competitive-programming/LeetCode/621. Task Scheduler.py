class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        letterFreq = Counter(tasks)

        pq = [-freq for freq in letterFreq.values()]
        heapq.heapify(pq)

        while pq:
            inCooldown = []
            currTime = 0
            for _ in range(n + 1):
                if pq:
                    highestFreq = heapq.heappop(pq)
                    currTime += 1

                    if highestFreq != -1:
                        # + 1 since using min heap
                        inCooldown.append(highestFreq + 1)
                else:
                    break

            for freq in inCooldown:
                heapq.heappush(pq, freq)

            if pq:
                # if freq still in pq we need to count these tasks as done and also idle
                res += n + 1
            else:
                # no idleing required
                res += currTime

        return res
