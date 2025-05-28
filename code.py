import numpy as np
import matplotlib.pyplot as plt
import gudhi as gd


points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [0.5, 0.866],  # forms a triangle
    [0.5, 0.3],    # inside point
    [0.2, 0.5]
])


rips_complex = gd.RipsComplex(points=points, max_edge_length=2.0)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=2)

print("Number of simplices:", simplex_tree.num_simplices())


simplex_tree.compute_persistence()


persistence = simplex_tree.persistence()
print("\nPersistence Intervals:")
for interval in persistence:
    print(interval)


plt.figure(figsize=(6, 5))
for dim, (birth, death) in persistence:
    if death != float('inf'):
        plt.scatter(birth, death, label=f"H{dim}", alpha=0.6)
    else:
        plt.scatter(birth, birth + 0.1, marker='x', label=f"H{dim} (∞)", alpha=0.6)

max_val = max(death if death != float('inf') else birth + 0.1 for _, (birth, death) in persistence)
plt.plot([0, max_val], [0, max_val], "k--", alpha=0.5)
plt.xlabel("Birth")
plt.ylabel("Death")
plt.title("Persistence Diagram")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 4))
for i, (dim, (birth, death)) in enumerate(persistence):
    if death == float('inf'):
        death = birth + 0.2  # visualize infinite bars
        linestyle = 'dashed'
    else:
        linestyle = 'solid'
    plt.hlines(y=i, xmin=birth, xmax=death, color='blue' if dim == 0 else 'green', linestyles=linestyle)
plt.xlabel("Filtration value")
plt.title("Persistence Barcode")
plt.tight_layout()
plt.show()
