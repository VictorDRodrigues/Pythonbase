import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]  # Valores no eixo x
y = [2, 4, 6, 8, 10]  # Valores no eixo y

# Criar o gráfico de linha
plt.plot(x, y)

# Adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar título ao gráfico
plt.title('Gráfico de Linha')

# Exibir o gráfico
plt.show()
