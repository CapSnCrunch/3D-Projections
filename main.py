import pygame
import pickle
import numpy as np

# TODO Fix rotations, forgot they aren't commutative in 3D :(

width = 750
height = 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('3D Projections')

scale = 100
origin = (width / 2, height / 2)
reference = [np.array([1, -1, 0]), np.array([1, 1, -2])]
vectors = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

class Poly():
    def __init__(self, color, points, edges):
        self.color = color
        self.vertices = []
        self.edges = edges

        self.get_vertices(points)
    
    def get_vertices(self, points):
        for p in points:
            self.vertices.append(np.array(p))
    
    def draw(self, win):
        #for i in range(len(self.vertices)):
        #    for j in range(i, len(self.vertices)):
        
        for e in self.edges:
            x1, y1 = proj(self.vertices[e[0]] * scale, reference[0], reference[1])
            x2, y2 = proj(self.vertices[e[1]] * scale, reference[0], reference[1])
            pygame.draw.line(win, self.color, (origin[0] + int(x1), origin[1] + int(y1)), (origin[0] + int(x2), origin[1] + int(y2)), 1)
    
    def rotate(self, r):
        for i in range(len(self.vertices)):
            self.vertices[i] = rotate(self.vertices[i], r)

def rotate_x(u, theta):
    R = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
    return R.dot(u)

def rotate_y(u, theta):
    R = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
    return R.dot(u)

def rotate_z(u, theta):
    R = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    return R.dot(u)

def rotate(u, r):
    return rotate_x(rotate_y(rotate_z(u, r[2]), r[1]), r[0])

def proj(u, vx, vy):
    # Normal Vector of Plane
    n = np.cross(vx, vy)
    n = n / np.sqrt(np.dot(n, n))

    # Vector Projection into Plane
    w = u - (np.dot(u, n) / np.dot(n, n)) * n

    # Change of Basis to Plane Vectors
    return (np.dot(w, vx) / np.sqrt(np.dot(vx, vx)), np.dot(w, vy) / np.sqrt(np.dot(vy, vy)))

def redraw_window(win, polyhedra):
    win.fill((250, 250, 250))

    # reference_rotate = [2*np.pi/200, 0, 2*np.pi/182]
    # reference_rotate = [0, 2*np.pi/850, 2*np.pi/1000]
    reference_rotate = [0, 0, 2*np.pi/1000]

    # polyhedra_rotate = [2*np.pi/200, 0, 0]
    polyhedra_rotate = [0, 0, 0]

    for i in range(len(vectors)):
        # Rotate Reference
        vectors[i] = rotate(vectors[i], reference_rotate)

        x, y = proj(vectors[i] * scale, reference[0], reference[1])
        pygame.draw.line(win, colors[i], origin, (origin[0] + int(x), origin[1] + int(y)), 2)
    
    for p in polyhedra:
        p.rotate(reference_rotate)
        p.rotate(polyhedra_rotate)
        p.draw(win)

    pygame.display.update()

with open('polyhedra.pkl', 'rb') as input:
    Tetrahedron = pickle.load(input)
    Tetrahedron2 = pickle.load(input)
    Cube = pickle.load(input)

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redraw_window(win, [Cube, Tetrahedron2])

if __name__ == '__main__':
    main()
else:
    pass