from collections import Counter

S = input()
char_cnts = Counter(S)

half = ""
center = ""

for ch in sorted(char_cnts):
    count = char_cnts[ch]
    
    if count % 2 == 1:
        if center:
            print("NO SOLUTION")
            exit()
        center = ch
    
    half += ch * (count // 2)

print(half + center + half[::-1])
