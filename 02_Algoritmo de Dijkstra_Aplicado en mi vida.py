#       Algoritmo de Dijkstra    #

# LEONARDO DANIEL RAMÍREZ MEDINA #
#        6E1   21310138          #
#        IA - 3ER PARCIAL        #

#Tema: Simulador de Algoritmo de Dijkstra - Aplicado en mi vida diaria  -  Transporte

#Descripción: El algoritmo de Dijkstra es un algoritmo de búsqueda de caminos más cortos.


def dijkstra(graph, start):             #Función que implementa el algoritmo de Dijkstra
    shortest_distances = {vertex: float('infinity') for vertex in graph}    #Inicializar las distancias más cortas
    shortest_distances[start] = 0                       #Establecer la distancia más corta al nodo de inicio como 0
    previous_vertices = {vertex: None for vertex in graph}      #Inicializar los vértices previos
    unvisited = graph.copy()                            #Crear una copia del grafo

    while unvisited:            #Mientras haya nodos no visitados
        current_vertex = min(unvisited, key=lambda vertex: shortest_distances[vertex])  #Seleccionar el nodo no visitado con la distancia más corta
        unvisited.pop(current_vertex)                   #Marcar el nodo como visitado

        for neighbour, distance in graph[current_vertex].items():   #Para cada vecino del nodo actual
            new_distance = shortest_distances[current_vertex] + distance    #Calcular la nueva distancia
            if new_distance < shortest_distances[neighbour]:    #Si la nueva distancia es menor que la distancia actual
                shortest_distances[neighbour] = new_distance    #Actualizar la distancia más corta
                previous_vertices[neighbour] = current_vertex   #Actualizar la distancia más corta y el vértice previo

    return previous_vertices, shortest_distances                #Retornar los vértices previos y las distancias más cortas

def reconstruct_path(previous_vertices, start, end):            #Función para reconstruir el camino más corto
    path = []                       #Inicializar el camino
    current_vertex = end                 #Inicializar el nodo actual como el nodo de destino
    while current_vertex != start:            #Mientras no se llegue al nodo de inicio
        path.append(current_vertex)         #Agregar el nodo actual al camino
        current_vertex = previous_vertices[current_vertex]      #Obtener el vértice previo
    path.append(start)                      #Agregar el nodo de inicio
    return path[::-1]                       #Retornar el camino en orden inverso

# Definimos el grafo de estaciones
graph = {
    "Periferico": {"Auditorio": 4, "Tetlan": 11},
    "Auditorio": {"Periferico": 4, "San Juan de Dios": 7},
    "San Juan de Dios": {"Auditorio": 7, "Juarez": 3},
    "Juarez": {"San Juan de Dios": 3, "Tetlan": 8},
    "Tetlan": {"Periferico": 11, "Juarez": 8}
}

# Simulación
start_station = input("Ingrese la estación de inicio: ")    #Pedir al usuario la estación de inicio
end_station = input("Ingrese la estación de destino: ")     #Pedir al usuario la estación de destino

previous_vertices, shortest_distances = dijkstra(graph, start_station)  #Aplicar el algoritmo de Dijkstra
path = reconstruct_path(previous_vertices, start_station, end_station)  #Reconstruir el camino más corto

print(f"Distancia más corta desde {start_station} a {end_station}: {shortest_distances[end_station]} km")   #Imprimir la distancia más corta
print(f"Ruta más corta: {' -> '.join(path)}")           #Imprimir la ruta más corta

import matplotlib.pyplot as plt     # se usa la librería matplotlib para graficar el grafo
import networkx as nx               # se usa la librería networkx para crear y manipular grafos

# Crear un grafo dirigido desde el diccionario
G = nx.DiGraph()        #Crear un grafo dirigido
for start, edges in graph.items():      #Para cada nodo y sus vecinos
    for end, weight in edges.items():   #Para cada vecino y su peso
        G.add_edge(start, end, weight=weight)   #Agregar un borde con su peso

# Posiciones de los nodos en un plano, puedes ajustar el layout según necesites
pos = nx.spring_layout(G)

# Dibujar el grafo
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')

# Dibujar los bordes de la ruta más corta con un color diferente
path_edges = list(zip(path, path[1:]))  #Obtener los bordes de la ruta más corta
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)  #Dibujar los bordes de la ruta más corta

# Etiquetas de peso en los bordes
edge_labels = nx.get_edge_attributes(G, 'weight')   #Obtener los pesos de los bordes
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)   #Dibujar las etiquetas de los bordes

plt.title("Ruta más corta")     #Título del gráfico
plt.show()  #Mostrar el gráfico