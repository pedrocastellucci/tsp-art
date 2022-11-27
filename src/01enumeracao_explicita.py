from utils import *

def backtrack(tour, left, N, coords, C, best=np.Inf, opt=None):
  if left == N:
    cost = get_cost(tour, C)
    if cost < best:
      best = cost
      opt = tour[:]
  else:
    for i in range(left, N):
      tour[left], tour[i] = tour[i], tour[left]           
      best, opt = backtrack(tour, left+1, N, coords, C, best, opt)
      tour[left], tour[i] = tour[i], tour[left]
  return best, opt

N = 6
nodes, coords = create_random_data(N)
C = get_dist_matrix(nodes, coords)
start = timer()
cost, tour = backtrack(nodes, 0, N, coords, C)
end = timer()
print(tour)
print(f"O tempo total foi de {end - start} segundos")
draw_route(tour, coords)