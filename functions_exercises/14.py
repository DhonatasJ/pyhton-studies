#CHAT GPT QUE FEZ 
def gerar_quadrado_magico(n):
    # Cria uma matriz vazia de ordem n x n
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    # Define a posição inicial
    i, j = n // 2, n - 1
    
    # Preenche a matriz com os números de 1 a n^2
    for num in range(1, n**2+1):
        matriz[i][j] = num
        
        # Verifica se a próxima posição está dentro da matriz e vazia
        if matriz[(i-1)%n][(j+1)%n] == 0:
            i, j = (i-1)%n, (j+1)%n
        else:
            i = (i+1)%n
    
    # Imprime o quadrado mágico
    for linha in matriz:
        print(linha)
        
# Exemplo de uso para gerar um quadrado mágico de ordem 3
gerar_quadrado_magico(3)


#CHAT GPT QUE FEZ 