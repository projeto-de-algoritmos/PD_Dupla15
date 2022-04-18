# Nessa questão, dados alguns arrays com tempo inicial, tempo final e lucro,
# é preciso retonar o lucro máximo que é possível conseguir.

# Temos "n" jobs

# Solução feita em Python3

from bisect import bisect_left

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        pd = []
        s = -1

        # Criar uma lista com as 3 variáveis a serem utilizadas
        job = list(zip(startTime, endTime, profit))
		
		# Fazemos a ordenação pelo tempo inicial
        job.sort(key=lambda x: startTime)
        
        # Criamos uma lista com os elementos iniciais da lista job para 
        # podermos modificá-lo à frente.
        aux = [job[i][0] for i in range(len(job)) ]
        
        # Criamos uma lista com elmentos "0" com tamanho da lista job para 
        # poder modificá-lo à frente.
        pd = [0 for _ in range(len(job))]
		
        # Bottom-up
        pd[len(job)+s] = job[len(job)+s][2]
        
        # for decrescente
        for i in range(len(job)-2, s, s):

			# Procura do 1° indíce onde a lista job termina
            index = bisect_left(aux, job[i][1], i, len(job))
			
			# Maior lucro
            aux1 = pd[i+1]

            if index < len(job):
                aux2 = pd[index] + job[i][2]
            else:
                aux2 = job[i][2]

            # A lista pd[] vai receber o max(aux1, aux2) de cada i

            if aux1 < aux2:
                aux3 = aux2

            else:
                aux3 = aux1

            pd[i] = aux3
        
        return pd[0]