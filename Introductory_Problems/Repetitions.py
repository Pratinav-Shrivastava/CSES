dna = input()

curr_len = 1
best_len = 1

for i in range(1, len(dna)):
    if dna[i] == dna[i - 1]:
        curr_len += 1
    else:
        curr_len = 1
    best_len = max(best_len, curr_len)

print(best_len)