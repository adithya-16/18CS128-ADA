edges = int(input("enter number of edges: "))
n_vertices = int(input("enter number of vertices: "))
graph = []
print("enter edges [start] [end] [weight]: ")
for i in range(edges):
    start, end, weight = [int(x) for x in input().split()]
    graph.append((start, end, weight))

def kruskals(graph):
        graph.sort(key=lambda e: e[2])
        included = set()
        for edge in graph:
                if edge[0] not in included or edge[1] not in included:
                        print(edge[0], '->', edge[1], '=', edge[2])
                        included.add(edge[0])
                        included.add(edge[1])
 
kruskals(graph.copy())

def count(S, m, n ): 
    if (n == 0): 
        return 1
    if (n < 0): 
        return 0; 
    if (m <=0 and n >= 1): 
        return 0
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] );
    
coins = [int(x) for x in input('enter coins: ').split()]
change = int(input('enter change: '))
print(count(coins, len(coins), change))