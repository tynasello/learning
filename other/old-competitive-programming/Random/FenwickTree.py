"""
dynamic variant of a prefix sum array. 
supports two O(logn) time operations on an array: processing a range sum query and updating a value.
 """

#  least siginifigant bit
def lsb(num):
    return num & -num


def buildFenwick(arr):
    fenwick = [0] + arr
    n = len(fenwick)

    for i in range(1, n):
        parent = i + lsb(i)
        if parent < n:
            fenwick[parent] += fenwick[i]
    return fenwick


def prefixSum(fenwick, num):
    # account for 1 based index of fenwick tree
    num += 1
    res = 0
    tree = fenwick
    while num != 0:
        res += tree[num]
        num -= lsb(num)

    return res


def pointUpdate(n, i, fenwick):
    tree = fenwick
    # account for 1 based index of fenwick tree
    i += 1
    while i <= len(tree):
        tree[i] += n
        i += lsb(i)
    return tree


if __name__ == "__main__":
    arr = [1, 3, 4, 8, 6, 2, 4, 2]
    fenwick = buildFenwick(arr)
    qs = [[1, 4], [0, len(arr) - 1]]
    print("-----------------------------")
    for q in qs:
        print("Array:", arr)
        print(
            "Query sum between",
            q,
            "=",
            prefixSum(fenwick, q[1]) - prefixSum(fenwick, q[0] - 1),
        )
        print("-----------------------------")
        arr[0] += 6
        arr[5] += 2
        fenwick = pointUpdate(6, 0, fenwick)
        fenwick = pointUpdate(2, 5, fenwick)
