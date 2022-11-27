from utils import *

def nearest_neighbor(locations, dist):
    n = len(locations)
    route = [0]
    unvisited = list(range(1, n))  # Zero is already in route
    while len(unvisited) != 0:
        pivot = route[-1]
        min_dist = np.inf
        nearest = None
        for j in unvisited:            
            if dist[pivot, j] < min_dist:
                min_dist = dist[pivot, j]
                nearest = j
        route.append(nearest)
        unvisited.remove(nearest)
    return route

file_tsp = "knight-500-stipple.tsp"  # Nome do arquivo .tsp contendo a instância
file_tsp = os.path.join("..", "images", file_tsp)
imagefile = file_tsp.replace(".tsp", ".png")
locations = read_data(file_tsp)  # Lê o arquivo com as posições de cada ponto
nodes = list(range(len(locations)))  # Gera uma lista com os nós da instância (0, ... n-1)
C = compute_euclidean_distance_matrix(locations)  # Compute a distância entre os pares
start = timer()
route = nearest_neighbor(nodes, C)  # Resolve a instância
end = timer()
cost = get_cost(route, C)  # Computa o custo da solução
draw_routes(imagefile, route, locations)  # Desenha a rota e gera a imagem
print(f"Custo da rota = {cost}, encontrado em {end-start} segundos")