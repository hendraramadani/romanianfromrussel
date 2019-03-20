dict_graph = {}


# Read the data.txt file
with open('data.txt', 'r') as f:
    for l in f:
        city_a, city_b, p_cost = l.split()
        if city_a not in dict_graph:
            dict_graph[city_a] = {}
        dict_graph[city_a][city_b] = int(p_cost)
        if city_b not in dict_graph:
            dict_graph[city_b] = {}
        dict_graph[city_b][city_a] = int(p_cost)


# Breadth First Search Method
def BreadthFirstSearch(graph, src, dst):
    q = [(src, [src], 0)]
    visited = {src}
    while q:
        (node, path, cost) = q.pop(0)
        for temp in graph[node].keys():
            if temp == dst:
                return path + [temp], cost + graph[node][temp]
            else:
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp, path + [temp], cost + graph[node][temp]))


# Depth First Search Method
def DepthFirstSearch(graph, src, dst):
    stack = []
    visited = {src}
    while stack:
        (node, path, cost) = stack.pop()
        for temp in graph[node].keys():
            if temp == dst:
                return path + [temp], cost + graph[node][temp]
            else:
                if temp not in visited:
                    visited.add(temp)
                    stack.append((temp, path + [temp], cost + graph[node][temp]))
                    
                    
# Iterative Deepening Search Method
def IterativeDeepening(graph, src, dst):
    level = 0
    count = 0
    stack = [(src, [src], 0)]
    visited = {src}
    while True:
        level += 1
        while stack:
            if count <= level:
                count = 0
                (node, path, cost) = stack.pop()
                for temp in graph[node].keys():
                    if temp == dst:
                        return path + [temp], cost + graph[node][temp]
                    else:
                        if temp not in visited:
                            visited.add(temp)
                            count += 1
                            stack.append((temp, path + [temp], cost + graph[node][temp]))
            else:
                q = stack
                visited_bfs = {src}
                while q:
                    (node, path, cost) = q.pop(0)
                    for temp in graph[node].keys():
                        if temp == dst:
                            return path + [temp], cost + graph[node][temp]
                        else:
                            if temp not in visited_bfs:
                                visited_bfs.add(temp)
                                q.append((temp, path + [temp], cost + graph[node][temp]))
                break


n = 1
print(dict_graph)
print("------------------------------------------------")

while n == 1:
    sch=int(input("1.BFS\n2.DFS\n3.ID\nEnter:"))
    
    if sch == 1:
        src = input("Enter the source: ")
        dst = input("Enter the Destination: ")
        while src not in dict_graph or dst not in dict_graph:
            print ("No such city name")
            src = input("Enter the correct source (case_sensitive):\n")
            dst = input("Enter the correct destination(case_sensitive):\n ")
        print ("for BFS")
        print (BreadthFirstSearch(dict_graph, src, dst))

    elif sch == 2:
        src = input("Enter the source: ")
        dst = input("Enter the Destination: ")
        while src not in dict_graph or dst not in dict_graph:
            print ("No such city name")
            src = input("Enter the correct source (case_sensitive):\n")
            dst = input("Enter the correct destination(case_sensitive):\n ")
        print ("for DFS")
        print (DepthFirstSearch(dict_graph, src, dst))

    elif sch == 3:
        src = input("Enter the source:")
        dst = input("Enter the Destination: ")
        while src not in dict_graph or dst not in dict_graph:
            print ("No such city name")
            src = input("Enter the correct source (case_sensitive):\n")
            dst = input("Enter the correct destination(case_sensitive):\n")
        print ("for ID")
        print (IterativeDeepening(dict_graph, src, dst))
      
    n=int(input("1.Continou\n2.Exit\nEnter:"))
