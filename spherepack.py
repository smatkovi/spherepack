import numpy as np
import trimesh

r = 3.0
mesh = trimesh.load_mesh('btr.stl')

print(trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[0][0])
print(trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[2][0])
print(trimesh.proximity.signed_distance(mesh, [[0.0, 0.0, 0.0]])[0] < 0)
print(mesh.face_normals[
	trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[2][0]])
print(trimesh.proximity.closest_point(mesh, [[-1590.88, 1158.07, 2755.49]]))
print(trimesh.proximity.signed_distance(mesh, [[-1590.88, 1158.07, 2755.49]]))

# if origin is outside of mesh
if trimesh.proximity.signed_distance(mesh, [[0.0, 0.0, 0.0]])[0] < 0:
# find nearest point on mesh and go a distance of a radius in negative direction of the normal to this nearest triangle on which this point is
	c_one = trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[0][0] - mesh.face_normals[ trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[2][0]] * r
	print(c_one)
	
