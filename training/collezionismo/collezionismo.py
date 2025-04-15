#!/usr/bin/env python3

import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

sys.stdin = open('C:\\Users\\Simon\\Desktop\\olympiads\\training\\collezionismo_input_1.txt')
sys.stdout = open('output.txt', 'w')

def solve(t):
    input()

    N, K = map(int, input().strip().split())

    C = list(map(int, input().strip().split()))

    # aggiungi codice...
    risposta = 0

    def min_discrepancy_sum_greedy(C, K):
        N = len(C)
        if K >= N:
            return 0  # ogni modellino su uno scaffale → discrepanza 0
        
        C.sort()
        
        # Calcola le differenze tra elementi adiacenti
        diffs = [C[i+1] - C[i] for i in range(N - 1)]
        
        # Ordina le differenze in ordine decrescente
        diffs.sort(reverse=True)
        
        # Somma totale della discrepanza se tutto fosse un gruppo
        total_discrepancy = C[-1] - C[0]
        
        # Sottrai le K-1 differenze più grandi → equivalgono a fare tagli lì
        return total_discrepancy - sum(diffs[:K-1])


    print(f"Case #{t}: {min_discrepancy_sum_greedy(C,K)}")


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()
