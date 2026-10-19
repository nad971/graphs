graph=[
    [0,4,0,0,7,2,0],
    [4,0,1,8,8,0,0],
    [0,1,0,0,3,0,0],
    [0,8,0,0,13,16,0],
    [7,8,0,13,0,0,0],
    [2,0,3,16,0,0,1],
    [0,0,0,0,0,1,0]
]
#кол-во вершин
def ver(graph):
    print("Колличество вершин:", len(graph))

#кол-во вершин у которых степень 3
count=0
for i in graph:
    k=0 #кол-во ненулевых элементов в строке
    for j in i:
        if graph[i][j] !=0:
            k+=1
        if k==3:
            count+=1
print("Колличество вершин со степенью 3:",count)

#кол-во ребер
count=0
for i in graph:
    for j in i:
        if j !=0:
            count+=1
print("Колличество ребер:", count//2)


#сумма весов всех ребер
def sum_edges(graph):
    count=0
    for i in graph:
        for j in i:
            count+=j
print("Сумма весов всех ребер:",count//2)


#кол-во соседей вершины F
count=0
for i in graph:
    for j in i:
        if graph[i][j]!=0:
            count+=1
print("Кол-во соседей вершины F:",count)
