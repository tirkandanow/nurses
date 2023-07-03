# Importowanie potrzebnych modułów
from docplex.mp.model import Model
import numpy as np

# Tworzenie modelu w CPLEX
model = Model(name='my_model')

# Tworzenie macierzy o wymiarach 10x7x3
matrix = np.array([[[2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4]],
                  [[5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7]],
                  [[8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1]],
                  [[2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4]],
                  [[5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7]],
                  [[8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1]],
                  [[2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4]],
                  [[5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7]],
                  [[8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1]],
                  [[2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4], [5, 6, 7], [8, 9, 1], [2, 3, 4]]])

# Pobieranie wymiarów macierzy
dim1, dim2, dim3 = matrix.shape

# Tworzenie zmiennych decyzyjnych w CPLEX
x = {(i, j, k): model.integer_var(name='x_{0}_{1}_{2}'.format(i, j, k)) for i in range(dim1) for j in range(dim2) for k in range(dim3)}

# Tworzenie ograniczeń dla zmiennych decyzyjnych
for i in range(dim1):
    for j in range(dim2):
        for k in range(dim3):
            model.add_constraint(x[i, j, k] == matrix[i, j, k])

# Definiowanie celu
# model.maximize(model.sum(x[i, j, k] for i in range(dim1) for j in range(dim2) for k in range(dim3)))
#
# # Rozwiązanie modelu
# solution = model.solve()

# Wyświetlanie rozwiązania
print(x)
