edges = int(input("enter number of edges: "))
n_vertices = int(input("enter number of vertices: "))
graph = {}
print("enter edges [start] [end] [weight]: ")
for i in range(edges):
    start, end, weight = [int(x) for x in input().split()]
    if not graph.get(start):
        graph[start] = [(end, weight)]
    else:
        graph[start].append((end, weight))

def prims(graph, startVertex):
	selected = set([startVertex])
	for no_edges in range(len(graph.keys()) - 1):
		end = None
		start = None
		weight = int(10e10)
		for startV in selected:
			for endV in graph[startV]:
				if endV[1] < weight and endV[0] not in selected:
					start, end, weight = startV, endV[0], endV[1] 
		print(f"{start} -> {end} = {weight}")
		selected.add(end)

prims(graph, 1)

def findPartition(arr, n): 
    sum = 0
    i, j = 0, 0
    for i in range(n): 
        sum += arr[i] 
    if sum % 2 != 0: 
        return false 
    part = [[ True for i in range(n + 1)]  
                   for j in range(sum // 2 + 1)] 
    for i in range(0, n + 1): 
        part[0][i] = True
    for i in range(1, sum // 2 + 1): 
        part[i][0] = False
    for i in range(1, sum // 2 + 1): 
        for j in range(1, n + 1): 
            part[i][j] = part[i][j - 1] 
            if i >= arr[j - 1]: 
                part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])  
    return part[sum // 2][n] 
     
arr = list(input('enter array: ').split())
n = len(arr) 
if findPartition(arr, n) == True: 
    print("Can be divided into two subsets of equal sum") 
else: 
    print("Can not be divided into two subsets of equal sum") 