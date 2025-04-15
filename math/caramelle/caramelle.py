#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys
import math

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
sys.stdin = open('C:\\Users\\Simon\\Desktop\\olympiads\\math\\input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    input()
    N = int(input().strip())


    V = list(map(int, input().strip().split()))

    c = 0


    # INSERISCI IL TUO CODICE QUI
    c = math.lcm(*V)

    print("Case #%d: " % test, end='')
    print(c)

sys.stdout.close()