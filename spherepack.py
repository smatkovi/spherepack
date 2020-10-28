import numpy as np
import trimesh

mesh = trimesh.load_mesh('btr.stl')
print(trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]]))
print(trimesh.proximity.signed_distance(mesh, [[0.0, 0.0, 0.0]]))
