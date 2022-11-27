from random import randint, sample
from timeit import default_timer as timer
import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import itertools
from PIL import Image, ImageDraw
import os

def get_dist_matrix(nodes, coords):
    n = len(nodes)
    C = np.zeros(shape=(n, n))
    for (i, j) in itertools.combinations(nodes, 2):    
        C[i, j] = C[j, i] = ((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2) ** 0.5
    return C

def create_random_data(N):
    nodes = list(range(N))
    coords = list(((randint(0, 100), randint(0, 100)) for _ in nodes))  
    return nodes, coords

def get_cost(tour, C):
    total = sum(C[n, tour[i+1]] for i, n in enumerate(tour[:-1]))
    return total + C[tour[-1], tour[0]]

def draw_route(tour, coords):
    data = []
    for i, p in enumerate(tour[:-1]):    
        x1, y1 = coords[p]
        x2, y2 = coords[tour[i+1]]
        plt.plot((x1, x2), (y1, y2), marker='o')
        plt.annotate(f"{p}", (x1+0.5, y1+0.5))
    x1, y1 = coords[tour[-1]]
    x2, y2 = coords[tour[0]]
    plt.plot((x1, x2), (y1, y2), marker='o')
    plt.annotate(f"{tour[-1]}", (x1+0.5, y1+0.5))
    plt.axis('equal')
    plt.show()

def read_data(inputfile):
    """Stores the data for the problem."""
    # Extracts coordinates from IMAGE_TSP and puts them into an array
    locations = []
    with open(inputfile) as f:
        for _ in range(6):
            next(f)
        for line in f:
            _,x,y = line.split()
            locations.append((int(float(x)),int(float(y))))
    return locations

 
def compute_euclidean_distance_matrix(locations):    
    dist = {}
    for i, p1 in enumerate(locations):
        for j, p2 in enumerate(locations):
            dist[i, j] = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    return dist


def draw_routes(image_file, route, locations):
    """Takes a set of nodes and a route, and outputs an image of the drawn TSP route"""
    tsp_path = []
    for j in route:        
        tsp_path.append((locations[j][0], locations[j][1]))
    tsp_path.append(tsp_path[0])
    original_image = Image.open(image_file)    
    width, height = original_image.size
    x, y = zip(*locations)

    tsp_image = Image.new("RGBA",(max(x),max(y)),color='white')
    tsp_image_draw = ImageDraw.Draw(tsp_image)
    #tsp_image_draw.point(tsp_path,fill='black')
    tsp_image_draw.line(tsp_path, fill='black', width=1)
    tsp_image = tsp_image.transpose(Image.FLIP_TOP_BOTTOM)
    final_image = image_file[:-4] + "-tsp.png"
    tsp_image.save(final_image)
    imshow(tsp_image)
    plt.show()
    print("TSP solution has been drawn and can be viewed at", final_image)


if __name__ == "__main__":
    pass