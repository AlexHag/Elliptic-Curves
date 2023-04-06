import numpy as np

def gamma_orbit(z):
    S = np.array([[0, -1], [1, 0]])
    T = np.array([[1, 1], [0, 1]])
    ST = np.dot(S, T)
    ST_inv = np.linalg.inv(ST)
    orbit = [z]

    for i in range(N):
        new_points = []
        for p in orbit:
            new_points.append(np.dot(S, p))
            new_points.append(np.dot(T, p))
            new_points.append(np.dot(ST, p))
            new_points.append(np.dot(ST_inv, p))
        orbit = np.unique(new_points, axis=0)

    return orbit

z = np.array([1, 1])
N = 3
orbit = gamma_orbit(z)
print("The first", N, "orbits of", z, "under PSL2Z are:")
for i in range(len(orbit)):
    print("Orbit", i+1, ":", orbit[i])