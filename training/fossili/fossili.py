#!/usr/bin/env python3

import sys

# Technically works, just is INSANELY slow with bigger arrays.
# only covers the first 3 test cases.

sys.stdin = open('C:\\Users\\Simon\\Desktop\\olympiads\\training\\fossili\\fossili_input_1.txt')
sys.stdout = open('output.txt', 'w')


def solve(t):
    input()
    a1, a2 = map(int, input().strip().split())
    b1, b2 = map(int, input().strip().split())
    c1, c2 = map(int, input().strip().split())

    # aggiungi codice...
    lasso1 = []
    lasso2 = []
    lasso3 = []

    for i in range(a1,a2):
        lasso1.append(i)
    
    for i in range(b1,b2):
        lasso2.append(i)

    for i in range(c1,c2):
        lasso3.append(i)

    anniInComune = set(lasso1).intersection(lasso2).intersection(lasso3)

    print(f"Case #{t}: {len(anniInComune)+1}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
