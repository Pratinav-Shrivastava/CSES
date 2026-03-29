def minimal_rotation(s):
    s2 = s + s
    n = len(s)
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        if s2[i + k] == s2[j + k]:
            k += 1
        elif s2[i + k] > s2[j + k]:
            i = i + k + 1
            if i <= j:
                i = j + 1
            k = 0
        else:
            j = j + k + 1
            if j <= i:
                j = i + 1
            k = 0
    start = min(i, j)
    return s2[start:start + n]

s = input().strip()
print(minimal_rotation(s))