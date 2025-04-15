
import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

sys.stdout = open('output.txt', 'w')
sys.stdin = open("input.txt", "r")

inputSplit = input().split(" ")

N = int(inputSplit[0]) # numero di corse da fare
M = int(inputSplit[1]) # numero corse in un singolo carnet
A = int(inputSplit[2]) # costo corsa singola
B = int(inputSplit[3]) # costo carnet

def solve(N, M, A, B):
    # Calcoliamo quante volte possiamo prendere un carnet
    num_carnets = N // M
    restante = N % M

    # Costo minimo per le corse piene
    costo_carnets = num_carnets * min(B, M * A)

    # Costo per le corse rimanenti
    costo_restante = min(restante * A, B)  # magari conviene un altro carnet

    print(costo_carnets + costo_restante)

solve(N,M,A,B)