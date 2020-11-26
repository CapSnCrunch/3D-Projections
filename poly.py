import pickle
from main import Poly

def save_objects(objects, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        for obj in objects:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

Tetrahedron = Poly((0,0,0),
    [[0,0,0],[1,0,1],[0,1,1],[1,1,0]],
    [[0,1],[0,2],[0,3],[1,2],[2,3],[3,1]])

Tetrahedron2 = Poly((0,0,0),
    [[-1,-1,-1],[1,1,-1],[1,-1,1],[-1,1,1]],
    [[0,1],[0,2],[0,3],[1,2],[2,3],[3,1]])

Cube = Poly((0,0,0), 
    [[-1,-1,-1],[-1,1,-1],[1,1,-1],[1,-1,-1],[-1,-1,1],[-1,1,1],[1,1,1],[1,-1,1]], 
    [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]])

with open('polyhedra.pkl', 'wb') as output:
    pickle.dump(Tetrahedron, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(Tetrahedron2, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(Cube, output, pickle.HIGHEST_PROTOCOL)

del Tetrahedron
del Tetrahedron2
del Cube

if __name__ == '__main__':
    pass