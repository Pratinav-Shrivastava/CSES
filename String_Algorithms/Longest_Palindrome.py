def longest_palindromic_substring(s: str) -> str:
    transformed = "#" + "#".join(s) + "#"
    n = len(transformed)
    P = [0] * n
    center = 0
    right = 0
    
    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            P[i] = min(right - i, P[mirror])
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and transformed[i + P[i] + 1] == transformed[i - P[i] - 1]:
            P[i] += 1
        if i + P[i] > right:
            center = i
            right = i + P[i]
    
    max_len, max_center = max((n, i) for i, n in enumerate(P))
    start = (max_center - max_len) // 2
    return s[start:start + max_len]

s = input().strip()
print(longest_palindromic_substring(s))