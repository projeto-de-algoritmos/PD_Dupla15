def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    # Construir a tabela K[][] de forma ascendente
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]],  
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
  
    return K[n][W]

while(True):
    n = int(input())

    if n==0:
        exit(0)

    numero_pizzas = int(input())

    pedidos = []
    tempos = []

    for i in range(n):
        pedido,tempo = map(int,input().split())
        pedidos.append(pedido)
        tempos.append(tempo)
    
    ans = knapSack(numero_pizzas, tempos, pedidos, n)
    ans = str(ans)

    print(ans+' min.')