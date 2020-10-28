import numpy as np
import trimesh

mesh = trimesh.load_mesh('btr.stl')
trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])
