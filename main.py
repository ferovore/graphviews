import graphviz

# Считывание списка смежности и перевод в список рёбер
def AdjListToEdges():
    k = 0
    for i in range(v):
        temp = [int(x) for x in file.readline().split()]
        for j in temp:
            if j > i + 1:
                edges[k] = [i + 1, j]
                k += 1

# Считывание матрицы смежности и перевод в список рёбер
def AdjMatrixToEdges():
    k = 0
    for i in range(v):
        temp = [int(x) for x in file.readline().split()]
        for j in range(v):
            if temp[j] and j > i:
                edges[k] = [i + 1, j + 1]
                k += 1

# Cчитывание матрицы инцедентности и перевод в список рёбер
def IncMatrixToEdges():
    for i in range(v):
        temp = [int(x) for x in file.readline().split()]
        for j in range(e):
            if temp[j]:
                if edges[j][0] == 0:
                    edges[j][0] = i + 1
                else:
                    edges[j][1] = i + 1

# Считывание списка рёбер
def ReadEdges():
    for i in range(e):
        edges[i][0], edges[i][1] = [int(x) for x in file.readline().split()]

file = open('gv_input.txt', 'r')
input_type = int(file.readline())                  # вид входных данных
v, e = [int(x) for x in file.readline().split()]   # количество вершин и рёбер

edges = [[0, 0] for i in range(e)]

if input_type == 1:
    AdjListToEdges()
elif input_type == 2:
    AdjMatrixToEdges()
elif input_type == 3:
    IncMatrixToEdges()
else:
    ReadEdges()

g = graphviz.Graph('G')
for i, j in edges:
    g.edge(str(i), str(j))

g.view('graph') # визуализация с помощью graphviz
