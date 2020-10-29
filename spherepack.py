import numpy as np
import trimesh

mesh = trimesh.load_mesh('btr.stl')
print(trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]]))
print(trimesh.proximity.signed_distance(mesh, [[0.0, 0.0, 0.0]]))
print(mesh.faces[13637])
print(trimesh.proximity.closest_point(mesh, [[-1587.11165215, 2258.88125697, 2753.24604090]]))
print(trimesh.proximity.signed_distance(mesh, [[-1587.11165215, 2258.88125697, 2753.24604090]]))
