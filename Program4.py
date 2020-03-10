digraph = {
	1 : [ False, [ 2, 3, 4 ] ],
	2 : [ False, [ 5, 6 ] ],
	3 : [ False, [ 7 ] ],
	4 : [ False, [ 8 ] ],
	5 : [ False, [ 9 ] ],
	6 : [ False, [ 9 ] ],
	7 : [ False, [ 9 ] ],
	8 : [ False, [ 9 ] ],
	9 : [ False, [ ] ],
}

graph = {
	1 : [ False, [ 2, 3, 4 ] ],
	2 : [ False, [ 1, 5, 6 ] ],
	3 : [ False, [ 1, 7 ] ],
	4 : [ False, [ 1, 8 ] ],
	5 : [ False, [ 2, 9 ] ],
	6 : [ False, [ 2, 9 ] ],
	7 : [ False, [ 3, 9 ] ],
	8 : [ False, [ 4, 9 ] ],
	9 : [ False, [ 5, 6, 7, 8] ]
}

start = 2

def clear(g):
	for key in g:
		g[key][0] = False

def bfs(g, s):
	q = [ s ]
	while q:
		node = q.pop(0)
		for ele in g[node][1]:
			if not g[ele][0]:
				q.append(ele)
		g[node][0] = True
	print("BFS:",end=" ")
	for key in g:
		if g[key][0]:
			print(key,end=" ")

def dfs(g, s):
	stack = [ s ]
	g[s][0] = True
	cycle = False
	while stack:
		i = 0
		node = stack[-1]
		if g[node][0]:
			cycle = True
		g[node][0] = True
		for ele in g[node][1]:
			if not g[ele][0]:
				stack.append(ele)
				break
			i += 1
		if i == len(g[node][1]):
			stack.pop(-1)
	for key in g:
		if not g[key][0]:
			print("\nNot connected graph")
			return
	print("\nConnected graph")
	if cycle:
		print("Graph has cycles")



clear(digraph)
bfs(digraph, start)
clear(graph)
dfs(graph, start)


