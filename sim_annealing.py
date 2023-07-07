import random
import math
import matplotlib.pyplot as plt


# Parametry
n = 10  # liczba pielęgniarek
d = 7  # liczba dni
z = 3  # liczba zmian
a1 = 3  # liczba pielęgniarek potrzebna na zmianę 1
a2 = 3  # liczba pielęgniarek potrzebna na zmianę 2
a3 = 2  # liczba pielęgniarek potrzebna na zmianę 3
c = 3  # liczba zmian, jaką ma wykonać pielęgniarka w tygodniu


# Preferencje pielęgniarek
p = [[[2, 3, 4, 5, 6, 7, 8], [9, 1, 2, 3, 4, 5, 6], [7, 8, 9, 1, 2, 3, 4]],
               [[5, 6, 7, 8, 9, 1, 2], [3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7]],
               [[8, 9, 1, 2, 3, 4, 5], [6, 7, 8, 9, 1, 2, 3], [4, 5, 6, 7, 8, 9, 1]],
               [[2, 3, 4, 5, 6, 7, 8], [9, 1, 2, 3, 4, 5, 6], [7, 8, 9, 1, 2, 3, 4]],
               [[5, 6, 7, 8, 9, 1, 2], [3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7]],
               [[8, 9, 1, 2, 3, 4, 5], [6, 7, 8, 9, 1, 2, 3], [4, 5, 6, 7, 8, 9, 1]],
               [[2, 3, 4, 5, 6, 7, 8], [9, 1, 2, 3, 4, 5, 6], [7, 8, 9, 1, 2, 3, 4]],
               [[5, 6, 7, 8, 9, 1, 2], [3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7]],
               [[8, 9, 1, 2, 3, 4, 5], [6, 7, 8, 9, 1, 2, 3], [4, 5, 6, 7, 8, 9, 1]],
               [[2, 3, 4, 5, 6, 7, 8], [9, 1, 2, 3, 4, 5, 6], [7, 8, 9, 1, 2, 3, 4]]]


def objective_func(solution):
    obj_func_val = 0
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            for k in range(len(solution[i][j])):
                obj_func_val += p[i][j][k] * solution[i][j][k]
    return obj_func_val


def generate_neighbour(solution):
    neighbour = solution.copy()
    i1 = random.randint(0, n - 1)
    i2 = random.randint(0, n - 1)
    j1 = random.randint(0, z - 1)
    j2 = random.randint(0, z - 1)
    k1 = random.randint(0, d - 1)
    k2 = random.randint(0, d - 1)
    neighbour[i1][j1][k1], neighbour[i2][j2][k2] = neighbour[i2][j2][k2], neighbour[i1][j1][k1]
    return neighbour


def acceptance_probability(delta_obj_func, temperature):
    return math.exp(-delta_obj_func / temperature)


# Wyżarzanie
def simulated_annealing(initial_temperature, final_temperature, cooling_rate, iterations_per_temperature):

    current_solution = [[[0] * d for _ in range(z)] for _ in range(n)]
    for i in range(n):
        for k in range(d):
            current_solution[i][random.randint(0, z - 1)][k] = 1

    current_obj_func = objective_func(current_solution)
    temperature = initial_temperature
    while temperature > final_temperature:
        for _ in range(iterations_per_temperature):
            neighbour_solution = generate_neighbour(current_solution)
            neighbour_obj_func = objective_func(neighbour_solution)
            delta_obj_func = neighbour_obj_func - current_obj_func

            if (
                    # kazda pielegniarka ma co najwyzej jedna zmiane w danym dniu
                    all(
                        sum(neighbour_solution[i][j][k] for j in range(z)) <= 1
                        for i in range(n)
                        for k in range(d)
                    )
                    # pielegniarka nie moze pracowac na pierwszej zmianie tuz po zmianie nocnej
                    and all(
                        neighbour_solution[i][2][k] + neighbour_solution[i][1][(k + 1) % d] <= 1
                        for i in range(n)
                        for k in range(d)
                    )
                    # kazda pielegniarka musi wykonac co najmniej c zmian w tygodniu
                    and all(
                        sum(neighbour_solution[i][j][k] for k in range(d)) >= c
                        for i in range(n)
                        for j in range(z)
                    )
                    # kazda pielegniarka ma co najmniej 1 dzien wolnego w harmonogramie tygodnia
                    and all(
                        sum(neighbour_solution[i][j][k] for k in range(d)) <= 6
                        for i in range(n)
                        for j in range(z)
                    )
                    # dla kazdej zmiany musi zgadzac sie liczba potrzebnych pielegniarek
                    and all(
                        sum(neighbour_solution[i][j][k] for j in range(z)) == a1
                        for i in range(n)
                        for k in range(d)
                    )
                    and all(
                        sum(neighbour_solution[i][j][k] for j in range(z)) == a2
                        for i in range(n)
                        for k in range(d)
                    )
                    and all(
                        sum(neighbour_solution[i][j][k] for j in range(z)) == a3
                        for i in range(n)
                        for k in range(d)
                    )
                    # pielegniarka nie moze wykonywac tej samej zmiany wiecej niz 2 razy pod rzad
                    and all(
                    sum(neighbour_solution[i][1][k],
                        neighbour_solution[i][1][(k + 1) % d],
                        neighbour_solution[i][1][(k + 2) % d],
                    ) <= 2
                    for i in range(n)
                    for k in range(d - 2)
                    )
                    and all(
                    sum(neighbour_solution[i][2][k],
                        neighbour_solution[i][2][(k + 1) % d],
                        neighbour_solution[i][2][(k + 2) % d],
                    ) <= 2
                    for i in range(n)
                    for k in range(d - 2)
                    )
                    and all(
                    sum(neighbour_solution[i][0][k],
                        neighbour_solution[i][0][(k + 1) % d],
                        neighbour_solution[i][0][(k + 2) % d],
                    ) <= 2
                    for i in range(n)
                    for k in range(d - 2)
                    )
                    # pielegniarka moze miec co najwyzej 3 zmiany nocne w tygodniu
                    and all(
                    sum(neighbour_solution[i][2][k] for k in range(d)) <= 3
                    for i in range(n)
                    )
            ):
                acceptance_prob = acceptance_probability(delta_obj_func, temperature)

                if delta_obj_func < 0 or random.random() < acceptance_prob:
                    current_solution = neighbour_solution
                    current_obj_func = neighbour_obj_func

        temperature *= cooling_rate

    final_solution = current_solution
    final_obj_func = current_obj_func
    return final_obj_func


final_val = simulated_annealing(initial_temperature=100.0, final_temperature=0.1, cooling_rate=0.95,
                                iterations_per_temperature=100)

print("Wartość funkcji celu: ", final_val)
