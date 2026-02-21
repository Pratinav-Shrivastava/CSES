def creating_strings_helper(s, path, used, result):
    if len(path) == len(s):
        result.append("".join(path))
        return
    
    for i in range(len(s)):
        if used[i] or (i>0 and s[i] == s[i-1] and not used[i-1]):
            continue

        used[i] = True
        path.append(s[i])

        creating_strings_helper(s, path, used, result)

        used[i] = False
        path.pop()

def creating_strings(s):
    s = sorted(s)
    result = []
    used = [False] * len(s)
    creating_strings_helper(s, [], used, result)

    unique_strings = sorted(set(result))
    return unique_strings

def solve():
        s = input()
        final_result = creating_strings(s)
        print(len(final_result))
        for perm in final_result:
            print(perm)

if __name__ == "__main__":
    solve()