import sys
import numpy as np
import trimesh

r = float(sys.argv[2])
print("radius =",r,"; file =",sys.argv[1])
eps = r * 0.01
centers = np.array([])
mesh = trimesh.load_mesh(sys.argv[1])
if mesh.is_watertight:
        print("approximately "+str(int(mesh.volume/(r*r*r*(22/7))))+" spheres")


# find nearest point on mesh and go a distance of a radius in negative direction of the normal to this nearest triangle on which this point is
c_prime = trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[0][0] - mesh.face_normals[ trimesh.proximity.closest_point(mesh, [[0.0, 0.0, 0.0]])[2][0] ] * r

centers = [c_prime] 

c_candidate = c_prime + np.array([2 * r, 0, 0])
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack((centers, [c_candidate]))
    
c_candidate = c_prime + (r * np.array([np.sqrt(3), 1, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))
	
c_candidate = c_prime + (r * np.array([-np.sqrt(3), 1, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([-2, 0, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))
	
c_candidate = c_prime + (r * np.array([-np.sqrt(3), -1, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))
	
c_candidate = c_prime + (r * np.array([np.sqrt(3), -1, 0]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))


c_candidate = c_prime + (r * 2 / np.sqrt(3) * np.array([0, -1, np.sqrt(2)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([1, 1/np.sqrt(3), 2*np.sqrt(2/3)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([-1, 1/np.sqrt(3), 2*np.sqrt(2/3)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))


c_candidate = c_prime + (r * 2 / np.sqrt(3) * np.array([0, -1, -np.sqrt(2)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([1, 1/np.sqrt(3), -2*np.sqrt(2/3)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))

c_candidate = c_prime + (r * np.array([-1, 1/np.sqrt(3), -2*np.sqrt(2/3)]))
if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps):
    centers = np.vstack(( centers, [c_candidate] ))


def arraydist(point):
    for c in reversed(centers):
        if np.sum((point - c)**2) < 4*r*r:
            return False
    return True


# c_prime = centers[1]
def new_env(c_prime):
    tempc = centers
    c_candidate = c_prime + np.array([2 * r, 0, 0])
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack((tempc, [c_candidate]))
        
    c_candidate = c_prime + (r * np.array([np.sqrt(3), 1, 0]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    	
    c_candidate = c_prime + (r * np.array([-np.sqrt(3), 1, 0]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    
    c_candidate = c_prime + (r * np.array([-2, 0, 0]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    	
    c_candidate = c_prime + (r * np.array([-np.sqrt(3), -1, 0]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    	
    c_candidate = c_prime + (r * np.array([np.sqrt(3), -1, 0]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    
    
    c_candidate = c_prime + (r * 2 / np.sqrt(3) * np.array([0, -1, np.sqrt(2)]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    
    c_candidate = c_prime + (r * np.array([1, 1/np.sqrt(3), 2*np.sqrt(2/3)]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    
    c_candidate = c_prime + (r * np.array([-1, 1/np.sqrt(3), 2*np.sqrt(2/3)]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    
    
    c_candidate = c_prime + (r * 2 / np.sqrt(3) * np.array([0, -1, -np.sqrt(2)]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    
    c_candidate = c_prime + (r * np.array([1, 1/np.sqrt(3), -2*np.sqrt(2/3)]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    
    c_candidate = c_prime + (r * np.array([-1, 1/np.sqrt(3), -2*np.sqrt(2/3)]))
    if trimesh.proximity.signed_distance(mesh, [c_candidate])[0]  > (r - eps) and arraydist(c_candidate):
        tempc = np.vstack(( tempc, [c_candidate] ))
    return tempc

surface = len(centers)
surface_old = 1
while surface_old < surface:
    for i in range(surface_old, surface):
        centers = new_env(centers[i])
    print(str(len(centers))+" spheres found yet")
    surface_old = surface
    surface = len(centers)
print(centers)
f = open(str(sys.argv[1])+".out", "a")
f.writelines(["%s\n" % item  for item in centers])
f.close()
