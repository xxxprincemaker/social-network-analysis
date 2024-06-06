from datetime import datetime

import numpy as np
from igraph import Graph, plot
import matplotlib.pyplot as plt
import csv
import matplotlib.cm as cm
import cairo
from PIL import Image
import matplotlib.patches as mpatches
import pandas as pd

MAX_ROWS = 286562


def create_graph_from_tsv(file_name, max_lines):
    g = Graph(directed=True)

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Ignora a primeira linha (cabeçalho)
        weights = []
        edges = []
        timestamp = []
        LIWC_ANX = []
        LIWC_ANG = []
        LIWC_SAD = []
        LIWC_BODY = []
        LIWC_HEALTH = []
        LIWC_MONEY = []
        LIWC_RELIG = []
        LIWC_DEATH = []
        for i, row in enumerate(reader):
            if i >= max_lines:
                break

            g.add_vertices([row[0], row[1]])
            edges.append((row[0], row[1]))
            weights.append(float(row[4]))  # Supondo que os pesos estejam na terceira coluna e sejam números flutuantes
            timestamp.append(row[3])
            LIWC_ANX.append(row[5][21])
            LIWC_ANG.append(row[5][22])
            LIWC_SAD.append(row[5][23])
            LIWC_BODY.append(row[5][24])
            LIWC_HEALTH.append(row[5][25])
            LIWC_MONEY.append(row[5][26])
            LIWC_RELIG.append(row[5][27])
            LIWC_DEATH.append(row[5][28])

        g.add_edges(edges)
        g.es['weight'] = weights
        g.es['timestamp'] = timestamp
        g.es['LIWC_ANX'] = LIWC_ANX
        g.es['LIWC_ANG'] = LIWC_ANG
        g.es['LIWC_SAD'] = LIWC_SAD
        g.es['LIWC_BODY'] = LIWC_BODY
        g.es['LIWC_HEALTH'] = LIWC_HEALTH
        g.es['LIWC_MONEY'] = LIWC_MONEY
        g.es['LIWC_RELIG'] = LIWC_RELIG
        g.es['LIWC_DEATH'] = LIWC_DEATH

    return g


# Use a função para criar um gráfico a partir de um arquivo .tsv
# Limitando a leitura a 10000 linhas
g = create_graph_from_tsv('Reddit_Hyperlinks_-_Processado.tsv', MAX_ROWS)

# Calcular a centralidade de grau
degree_centrality = g.degree()

# Calcular os scores de authority
authority_scores = g.authority_score()

# Calcular os scores de PageRank
pagerank_scores = g.pagerank()

# Criar uma lista de tuplas (vértice, centralidade de grau, score de authority, score de PageRank)
vertices_scores = [(vertex, degree_centrality[i], authority_scores[i], pagerank_scores[i]) for i, vertex in enumerate(g.vs)]

# Ordenar a lista com base na centralidade de grau, score de authority e score de PageRank em ordem decrescente
vertices_scores.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

# Selecionar os top 10 vértices
top_vertices = vertices_scores[:10]

# Imprimir os top 10 vértices
print("\nTop 10 Subcomunidades Mais Influentes:")
for i, (vertex, degree, authority, pagerank) in enumerate(top_vertices, 1):
    print(f"{i}. {vertex['name']}: Centralidade de Grau = {degree}, Authority Score = {authority}, PageRank Score = {pagerank}")

# Inicializar um dicionário para armazenar o número de arestas negativas para cada vértice
negative_edge_counts = {vertex: 0 for vertex in g.vs}

# Iterar sobre todas as arestas do grafo
for edge in g.es:
    # Se o peso da aresta é negativo e o vértice de origem da aresta é o vértice atual, incrementar o contador
    if edge['weight'] < 0:
        negative_edge_counts[g.vs[edge.source]] += 1

# Ordenar os vértices com base no número de arestas negativas em ordem decrescente
sorted_vertices = sorted(negative_edge_counts.items(), key=lambda x: x[1], reverse=True)

# Selecionar os top 10 vértices
top_vertices = sorted_vertices[:10]

# Imprimir os top 10 vértices
print("\nTop 10 Comunidades Mais Tóxicas:")
for i, (vertex, count) in enumerate(top_vertices, 1):
    print(f"{i}. {vertex['name']}: {count} arestas negativas saindo")

# # Convert the graph to undirected
# g_undirected = g.as_undirected()
#
# # Now you can apply the function that requires an undirected graph
# # For example, if you were trying to calculate the modularity
# communities = g_undirected.community_fastgreedy().as_clustering()
# # Ordenar as comunidades pelo tamanho
# sorted_communities = sorted(communities, key=len, reverse=True)
#
# # Selecionar as 10 maiores comunidades
# top_communities = sorted_communities[:10]
#
# # Imprimir as 10 maiores comunidades e a quantidade de subreddits que fazem parte de cada comunidade
# print("\n")
# for i, community in enumerate(top_communities, 1):
#     print(f"Comunidade {i} (tamanho: {len(community)} subreddits")