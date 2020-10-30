import numpy as np
import trimesh

mesh = trimesh.load_mesh('btr.stl')
print(trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]]))
print(trimesh.proximity.signed_distance(mesh, [[0.0, 0.0, 0.0]]))
print(mesh.face_normals[13637])
print(trimesh.proximity.closest_point(mesh, [[-1590.88, 1158.07, 2755.49]]))
print(trimesh.proximity.signed_distance(mesh, [[-1590.88, 1158.07, 2755.49]]))
