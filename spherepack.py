import numpy
from stl import mesh

# Using an existing stl file:
your_mesh = mesh.Mesh.from_file('btr.stl')

# The mesh normals (calculated automatically)
print('normals')
print(your_mesh.normals)
# The mesh vectors
print('vectors')
print(your_mesh.v0, your_mesh.v1, your_mesh.v2)
