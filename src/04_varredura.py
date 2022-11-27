from utils import *

def sweep(nodes, coords):
    tour = sorted(nodes, key=lambda x: np.arctan(coords[x][1]/(coords[x][0] + 1e-3)))
    return tour 

N = 10
nodes, coords = create_random_data(N)
C = get_dist_matrix(nodes, coords)
start = timer()
tour = sweep(nodes, coords)
end = timer()
print(f"O tempo total foi de {end - start} segundos")
draw_route(tour, coords)