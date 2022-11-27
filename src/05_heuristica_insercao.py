from utils import *

def insertion_heur(_nodes, C):
    tour = [_nodes[0], _nodes[1]]
    nodes = _nodes[2:]  
    while len(nodes) != 0:
        pidx = randint(0, len(nodes)-1)
        p = nodes[pidx]
        nodes.pop(pidx)
        min_addcost = C[tour[-1], p] + C[p, tour[0]] - C[tour[-1], tour[0]]
        addidx = 0
        i = 1
        n = len(tour)
        while i < n:      
            cand = C[tour[i-1], p] + C[p, tour[i]] - C[tour[i-1], tour[i]]
            if cand < min_addcost:
                min_addcost = cand
                addidx = i
            i = i + 1
        tour.insert(addidx, p)
    return tour

N = 500
nodes, coords = create_random_data(N)
C = get_dist_matrix(nodes, coords)
start = timer()
tour = insertion_heur(nodes, C)
end = timer()
print(f"O tempo total foi de {end - start} segundos")
draw_route(tour, coords)