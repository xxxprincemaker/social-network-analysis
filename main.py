# Importando a biblioteca
from igraph import Graph, plot

# Criando um gráfico simples
g = Graph()

# Adicionando vertices ao gráfico
g.add_vertices(3)

# Adicionando arestas ao gráfico
g.add_edges([(0,1), (1,2)])

# Plotando o gráfico
plot(g, "graph.png", bbox=(200,200), layout = g.layout("kk"))
