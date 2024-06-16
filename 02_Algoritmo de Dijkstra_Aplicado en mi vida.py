#       Algoritmo de Dijkstra    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Simulador de Algoritmo de Dijkstra - Aplicado en mi vida diaria  -  Transporte


def dijkstra(graph, start):
    shortest_distances = {vertex: float('infinity') for vertex in graph}
    shortest_distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    unvisited = graph.copy()

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: shortest_distances[vertex])
        unvisited.pop(current_vertex)

        for neighbour, distance in graph[current_vertex].items():
            new_distance = shortest_distances[current_vertex] + distance
            if new_distance < shortest_distances[neighbour]:
                shortest_distances[neighbour] = new_distance
                previous_vertices[neighbour] = current_vertex

    return previous_vertices, shortest_distances

def reconstruct_path(previous_vertices, start, end):
    path = []
    current_vertex = end
    while current_vertex != start:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.append(start)
    return path[::-1]

# Definir el grafo de estaciones
graph = {
    "Periferico": {"Auditorio": 4, "Tetlan": 11},
    "Auditorio": {"Periferico": 4, "San Juan de Dios": 7},
    "San Juan de Dios": {"Auditorio": 7, "Juarez": 3},
    "Juarez": {"San Juan de Dios": 3, "Tetlan": 8},
    "Tetlan": {"Periferico": 11, "Juarez": 8}
}

# Simulación
start_station = input("Ingrese la estación de inicio: ")
end_station = input("Ingrese la estación de destino: ")

previous_vertices, shortest_distances = dijkstra(graph, start_station)
path = reconstruct_path(previous_vertices, start_station, end_station)

print(f"Distancia más corta desde {start_station} a {end_station}: {shortest_distances[end_station]} km")
print(f"Ruta más corta: {' -> '.join(path)}")

import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo dirigido desde el diccionario
G = nx.DiGraph()
for start, edges in graph.items():
    for end, weight in edges.items():
        G.add_edge(start, end, weight=weight)

# Posiciones de los nodos en un plano, puedes ajustar el layout según necesites
pos = nx.spring_layout(G)

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')

# Dibujar los bordes de la ruta más corta con un color diferente
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# Etiquetas de peso en los bordes
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Ruta más corta")
plt.show()