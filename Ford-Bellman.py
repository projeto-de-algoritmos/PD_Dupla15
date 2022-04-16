def bellmonFord(n, m, src, dest, edges):
    # Esta etapa inicializa as distâncias da fonte para todos os vértices como infinitas
    d = [1000000000 for i in range(n + 1)]
    
    # Distância da própria fonte como 0
    d[src] = 0
    
    # Esta etapa calcula as distâncias mais curtas. Fazendo o loop |V|-1 vezes onde |V| é o número de vértices no grafo dado
    for i in range(1, n):
        for u,v,w in edges:
            if (d[u] != 1000000000 and d[v] > (d[u] + w)):
                d[v] = d[u] + w
                
    # Retorna o peso da origem até o destino especificado
    return d[dest]