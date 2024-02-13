class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counter = collections.Counter(s)
        chars = sorted(list(s), key=lambda c: (counter[c]*-1, c))

        if (counter[chars[0]] > (n+1)//2):
            return ''

        res = ['-'] * n
        charsi = 0

        for i in range(0, n, 2):
            res[i] = chars[charsi]
            charsi += 1
        for i in range(1, n, 2):
            res[i] = chars[charsi]
            charsi += 1

        return ''.join(res)

    # def reorganizeString(self, s: str) -> str:
    #     n = len(s)
    #     counter = collections.Counter(s)

    #     maxheap = [(value*-1, key) for key, value in counter.items()]
    #     heapq.heapify(maxheap)

    #     i = 0
    #     res = ['-'] * n

    #     tempval = 0
    #     tempkey = 0

    #     while (maxheap):

    #         val, key = heapq.heappop(maxheap)

    #         res[i] = key
    #         i += 1

    #         if (tempval < 0):
    #             heapq.heappush(maxheap, (tempval, tempkey))

    #         tempval = val+1
    #         tempkey = key

    #     if (res[-1] == "-"):
    #         return ""

    #     return "".join(res)
