#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

sys.stdin = open('C:\\Users\\Simon\\Desktop\\olympiads\\rec\\input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    input()
    N1, N2, N3, N4 = map(int, input().strip().split())

    M = int(input().strip())

    F1 = input().strip()

    F2 = input().strip()

    F3 = input().strip()

    F4 = input().strip()

    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0

    # INSERISCI IL TUO CODICE QUI

    words = [F1, F2, F3, F4]
    substring_sets = []
    for word in words:
        substrings = {word[i:i+ M] for i in range(len(word) - M + 1)}
        substring_sets.append(substrings)

    common_substrings = set.intersection(*substring_sets)

    for x in common_substrings:
        p1 = F1.index(x)
        p2 = F2.index(x)
        p3 = F3.index(x)
        p4 = F4.index(x)

    print("Case #%d: " % test, end='')
    print(p1, p2, p3, p4)

sys.stdout.close()