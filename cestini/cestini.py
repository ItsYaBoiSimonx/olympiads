
import sys

sys.stdin = open('C:\\Users\\Simon\\Desktop\\olympiads\\cestini\\input.txt')
sys.stdout = open('output.txt', 'w')

def solve(t):
    input() # Prima riga vuota

    N, M, Q = map(int, input().strip().split())
    S = input().strip()
    # Aggiungi codice se vuoi
    risposta = []
    matrice = [list(S)]

    for i in range(M-1):
        matrice.append([])

    for i in range(Q):
        w, *args = input().strip().split()
        a, b = map(int, args)

        if w == 's':
            matrice[b].append(matrice[a][len(matrice[a])-1])
            matrice[a].pop(len(matrice[a])-1)
            pass

        elif w == 'c':
            # c 0 163989
            risposta.append(matrice[a][b])


    print(f"Case #{t}:", ''.join(risposta))


T = int(input().strip())

for t in range(1, T+1):
    solve(t)

sys.stdout.close()