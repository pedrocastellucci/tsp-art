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

def get_2opt_savings(route, i, j, dist):
    n = len(route)
    i0, i1 = route[i], route[i+1]
    j0, j1 = route[j], route[(j+1) % n]
    savings = dist[i0, i1] + dist[j0, j1]    
    savings = savings - dist[i0, j0] - dist[i1, j1]
    return savings

def get_improved_2opt(route, dist):
    n = len(route)    
    best_i, best_j = None, None
    best_save = 0
    for i in range(n-3):
        for j in range(i+2, n):      
            if (j + 1) % n == i:
                continue
            save = get_2opt_savings(route, i, j, dist)
            if save > best_save:
                best_save = save
                best_i, best_j = i, j

    if best_i is not None:
        i, j = best_i, best_j
        return route[:i+1] + list(reversed(route[i+1:j+1])) + route[j+1:], best_save
    return route, best_save


def local_search(route, dist):
    cand_sol, save = get_improved_2opt(route, dist)
    while save > 1e-4:
        route = cand_sol
        cand_sol, save = get_improved_2opt(route, dist)
        print(f"Encontrou solução economizando {save}")
    return route   


file_tsp = "knight-1000-stipple.tsp"  # Nome do arquivo .tsp contendo a instância
file_tsp = os.path.join("..", "images", file_tsp)
imagefile = file_tsp.replace(".tsp", ".png")
locations = read_data(file_tsp)  # Lê o arquivo com as posições de cada ponto
nodes = list(range(len(locations)))  # Gera uma lista com os nós da instância (0, ... n-1)
C = compute_euclidean_distance_matrix(locations)  # Compute a distância entre os pares
start = timer()
route = nearest_neighbor(locations, C)
route = local_search(route, C)
end = timer()
cost = get_cost(route, C)  # Computa o custo da solução
draw_routes(imagefile, route, locations)  # Desenha a rota e gera a imagem
print(f"Custo da rota = {cost}, encontrado em {end-start} segundos")