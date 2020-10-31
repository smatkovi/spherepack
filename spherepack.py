import numpy as np
import trimesh

r = 3.0
eps = r * 0.01
centers = np.array([])
mesh = trimesh.load_mesh('btr.stl')

print(trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]]))
print(trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]]))
print(trimesh.proximity.signed_distance(mesh, [[0.0, 0.0, 0.0]])[0] < 0)
print(mesh.face_normals[
	trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[2][0]])



# find nearest point on mesh and go a distance of a radius in negative direction of the normal to this nearest triangle on which this point is
c_prime = trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[0][0] - mesh.face_normals[ trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[2][0] ] * r

centers = [c_prime] 

c_candidate = c_prime + np.array([2 * r, 0, 0])
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack((centers, [c_candidate]))
    
c_candidate = c_prime + (r * np.array([np.sqrt(3), 1, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))
	
c_candidate = c_prime + (r * np.array([-np.sqrt(3), 1, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([-2, 0, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))
	
c_candidate = c_prime + (r * np.array([-np.sqrt(3), -1, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))
	
c_candidate = c_prime + (r * np.array([np.sqrt(3), -1, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))


c_candidate = c_prime + (r * 2 / np.sqrt(3) * np.array([0, -1, np.sqrt(2)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([1, 1/np.sqrt(3), 2*np.sqrt(2/3)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([-1, 1/np.sqrt(3), 2*np.sqrt(2/3)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * 2 / np.sqrt(3) * np.array([0, -1, -np.sqrt(2)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([1, 1/np.sqrt(3), -2*np.sqrt(2/3)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([-1, 1/np.sqrt(3), -2*np.sqrt(2/3)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0] > 0:
    centers = np.vstack(( centers, [c_candidate] ))
print(centers)
