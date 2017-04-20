def removeDuplicates(A):
    if not A:
        return 0
    counts = 1
    for i in range(1, len(A)):
        if A[i - 1] != A[i]:
            counts += 1
    return counts
if __name__ == "__main__":
    arr = [int(x) for x in input().strip().split()]
    arr = sorted(arr)
    result = removeDuplicates(arr)
    print(result)