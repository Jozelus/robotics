import numpy as np

def probability(values, entries, colors):
    results = np.zeros((colors, 3))
    for i in range(len(values)):
        results[i][0] = values[i][0] / entries 
        results[i][1] = values[i][1] / values[i][0]
        results[i][2] = results[i][0] * results[i][1]
    return results

def print_results(res):
    print("Color, marginal, conditional, joint")
    for i in range(len(res)):
        print(str(i), end="")
        for y in range(3):
            print(" " + str(res[i][y]), end="")
        print()

colors = 10

data = np.loadtxt("data.txt", dtype=np.int16)

values = np.zeros((colors, 5), dtype=np.int16)

for i in range(len(data)):
    values[data[i][0]][1] += data[i][1]
    values[data[i][0]][0] += 1

results = probability(values, len(data), colors)
print_results(results)
