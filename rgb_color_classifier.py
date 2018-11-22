import math

memory = {}


def train(values, labels):
    for i in range(0, len(values)):
        memory[values[i]] = labels[i]


def find_nearest_neighbor(rgb_tuple):
    distances = {}
    for i in memory:
        distances[i] = distance(i, rgb_tuple)

    sorted_distances = sorted(distances.items(), key=lambda t: t[1], reverse=True)
    return memory[sorted_distances[0][0]]


def distance(t1, t2):
    x_diff = t1[0] - t2[0]
    y_diff = t1[1] - t2[1]
    z_diff = t1[2] - t2[2]
    return math.sqrt(x_diff ** 2 + y_diff ** 2 + z_diff ** 2)


values = [(0, 0, 0), (255, 0, 0), (255, 127, 80), (220, 20, 60), (0, 255, 255), (169, 169, 169), (255, 140, 0),
          (255, 140, 0), (255, 140, 0)]
labels = ["black", "red", "coral", "crimson", "cyan", "dark grey", "dark orange", "deep pink", "fuchsia"]

train(values, labels)

print find_nearest_neighbor((204, 45, 99))

print memory
