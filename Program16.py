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

def dijkstra(graph, src):
	distance = [float('INF')] * n_vertices
	distance[src] = 0
	selected = [(src, distance[src])]
	curr_vertex = src

	while len(selected) < n_vertices:
		min_vertex, min_dist = -1, float('inf')
		
		# update distances from that vertex
		for neighbour in graph[curr_vertex]:
			vertex, weight = neighbour
			distance[vertex] = min(distance[curr_vertex] + weight, distance[vertex])
			
		# find vertex with min distance
		for vertex in range(n_vertices):
			if distance[vertex] <= min_dist and (vertex, distance[vertex]) not in selected:
				min_vertex, min_dist = vertex, distance[vertex]
		
		# add vertex and minimum distance to selected
		selected.append((min_vertex, min_dist))
		# update curr_vertex
		curr_vertex = min_vertex

	print('Vertex\tDistance')
	[print(vertex, '\t', distance, sep='') for vertex, distance in selected]

dijkstra(graph, int(input('enter source vertex: ')))

def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo

def lengthOfLIS(nums):       
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)
        
lengthOfLIS([int(x) for x in input('enter numbers: ').split()])