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

N = 10
nodes, coords = create_random_data(N)
C = get_dist_matrix(nodes, coords)
start = timer()
tour = nearest_neighbor(coords, C)
end = timer()
print(f"O tempo total foi de {end - start} segundos")
draw_route(tour, coords)