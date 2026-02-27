#Exemplo de rede neural MLP
import numpy as np

# Entradas
x = np.array([1, 2])

# Pesos da camada oculta
w1 = np.array([[0.5, -0.4],
               [0.3, 0.8],
               [-0.6, -0.2]])

b1 = np.array([0.1, 0.2, 0.5])

def relu(z):
    return np.maximum(0, z)

# Cálculo de z1, z2, z3
z1 = w1 @ x + b1
a1 = relu(z1)

# Pesos e bias da camada de saida
w2 = np.array([0.7, -0.5, 0.9])
b2 = 0.2

# Saída
z2 = w2 @ a1 + b2

# Função sigmóide (classificação)
def sigmoide(z):
    return 1 / (1 + np.exp(-z))

# Saída Final
y_regressao = z2
y_classificacao = sigmoide(z2)

# Exibe os resultados
print ("Saída para regressão: ", y_regressao)
print ("Saída para classificação: ", y_classificacao)
