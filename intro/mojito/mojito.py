#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

sys.stdin = open('C:\\Users\\Simon\\Desktop\\olympiads\\intro\\mojito\\input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())


for test in range(1, T+1):
    input()
    capacita, video, canzoni = map(int, input().strip().split())
    contatore = 0
    nvideo = 0
    ncanzoni = 0

    while capacita > contatore:
        contatore += video
        nvideo += 1
        if contatore > capacita:
            nvideo -= 1
            contatore -= video
            while capacita > contatore:
                contatore += canzoni
                ncanzoni += 1
                if contatore > capacita:
                    ncanzoni -= 1
                    break


    print("Case #%d: " % test, end='')
    print(nvideo, ncanzoni)

sys.stdout.close()