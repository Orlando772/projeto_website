N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
 
def calcula_custo(paridade_inicio):
   """
   paridade_inicio = 0 -> começa com par no canto superior esquerdo
   paridade_inicio = 1 -> começa com ímpar no canto superior esquerdo
   Retorna (custo_total, nova_matriz)
   """
   custo = 0
   nova = [[0] * M for _ in range(N)]
   for i in range(N):
       for j in range(M):
         
           esperado = (paridade_inicio + i + j) % 2  # 0 = par, 1 = ímpar
           atual = grid[i][j] % 2
           if atual != esperado:
               
               nova[i][j] = grid[i][j] + 1
               custo += 1
           else:
               nova[i][j] = grid[i][j]
   return custo, nova
# Testa os dois
custo1, matriz1 = calcula_custo(0)  # canto superior esquerdo par
custo2, matriz2 = calcula_custo(1)  # canto superior esquerdo impar
# Escolhe o melhor
if custo1 <= custo2:
   print(custo1)
   for linha in matriz1:
       print(*linha)
else:
   print(custo2)
   for linha in matriz2:
       print(*linha)
 