import matplotlib.pyplot as plt

# Número de iterações para atingir equilíbrio
MAX = 100
r = float(input("Entre com a constante r: "))
x = float(input("Entre com x0: "))
population = [x]
for i in range(1, MAX):
    x = r * x * (1 - x)
    population.append(x)
print("População no longo prazo: ", population[-1])
# Plota gráfico da população pelo tempo
eixox = list(range(MAX))
plt.figure(1)
plt.plot(eixox, population)
plt.show()
