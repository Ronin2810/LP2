# def sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if(arr[min_index]>arr[j]):
#                 min_index=j
        
#         arr[min_index],arr[i] = arr[i],arr[min_index]
    
#     return arr

# a = [5,4,3,2,1]
# print(a)
# ans = sort(a)
# print(ans)


# from collections import defaultdict
# def bfs(graph,start,visited=None,queue=None):
#     if visited is None:
#         visited = set()
#     if queue is None:
#         queue = []
#     visited.add(start)
#     print(start,end=" ")
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)
#     if queue:
#         bfs(graph,queue.pop(0),visited,queue)

# def dfs(graph,start,visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start,end=" ")
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph,neighbor,visited)

# graph = defaultdict(list)
# num = int(input("Enter number of vertices: "))
# for i in range(num):
#     neighbors  = (input(f"Enter neighbors of {i}: ").split())
#     graph[i] = [int(neighbor) for neighbor in neighbors]

# start = int(input("Enter Starting vertex: "))
# print("BFS: ")
# bfs(graph, start)
# print("\nDFS: ")
# dfs(graph, start)



# g=0
# def print_board(start):
#     for i in range(9):
#         if i%3==0:
#             print()
#         if start[i]==-1:
#             print("_",end=" ")
#         else:
#             print(start[i],end=" ")
#     print()

# def solvable(start):
#     inv=0
#     for i in range(9):
#         if start[i]<=1:
#             continue
#         for j in range(i+1,9):
#             if start[j]==-1:
#                 continue
#             if start[i]>start[j]:
#                 inv+=1
    
#     if inv%2==0:
#         return True
#     else:
#         return False

# def heurustic(start,goal):
#     global g
#     h=0
#     for i in range(9):
#         for j in range(9):
#             if(start[i]==goal[j] and start[i]!=-1):
#                 h += (abs(j-i)// 3+ (abs(j-i)%3))
#     return h+g

# def left(start,pos):
#     start[pos],start[pos-1] = start[pos-1],start[pos]

# def right(start,pos):
#     start[pos],start[pos+1] = start[pos+1],start[pos]

# def up(start,pos):
#     start[pos],start[pos-3] = start[pos-3],start[pos]

# def down(start,pos):
#     start[pos],start[pos+3] = start[pos+3],start[pos]

# def movetile(start,goal):

#     emptyat = start.index(-1)
#     row= emptyat//3
#     col=emptyat%3

#     t1,t2,t3,t4 = start[:],start[:],start[:],start[:]
#     f1,f2,f3,f4 = 100, 100, 100, 100

#     if col-1>=0:
#         left(t1,emptyat)
#         f1 = heurustic(t1,goal)
#     if col+1<3:
#         right(t2,emptyat)
#         f2 = heurustic(t2,goal)

#     if row+1<3:
#         down(t3,emptyat)
#         f3 = heurustic(t3,goal)

#     if row-1>=0:
#         up(t4,emptyat)
#         f4 = heurustic(t4,goal)

#     min_heuristic = min(f1, f2, f3, f4)

#     if f1 == min_heuristic:
#         left(start, emptyat)
#     elif f2 == min_heuristic:
#         right(start, emptyat)
#     elif f3 == min_heuristic:
#         down(start, emptyat)
#     elif f4 == min_heuristic:
#         up(start, emptyat)

# def solve(start,goal):
#     global g
#     g+=1
#     movetile(start,goal)
#     print_board(start)
#     f = heurustic(start,goal)
#     if f==g:
#         print(f"Solved in {f} moves")
#         return
#     solve(start,goal)

# def main():
#     global g
#     start = list()
#     goal = list()
#     print("\n Enter the start state (3x3 matrix, enter -1 for empty):")
#     for _ in range(3):
#         line = input().split()
#         start += [int(x) for x in line]

#     print("\n Enter the goal state (3x3 matrix, enter -1 for empty):")
#     for _ in range(3):
#         line = input().split()
#         goal += [int(x) for x in line]

#     print_board(start)

#     # To check if solvable
#     if solvable(start):
#         solve(start, goal)
#     else:
#         print("Not possible to solve")

# if __name__ == '__main__':
#     main()



# import sys
# import heapq

# class Graph:
#     def __init__(self,n):
#         self.n = n
#         self.adj_list = [[] for i in range(n)]
    
#     def add_edge(self,src,dest,wt):
#         self.adj_list[src].append((dest,wt))
#         self.adj_list[dest].append((src,wt))
    
#     def dijkstra(self,src):
#         #setting all distances as infinity
#         distances = [sys.maxsize]*self.n
#         distances[src]=0

#         priority_q = [(0,src)]

#         while priority_q:
#             dist,curr_vert = heapq.heappop(priority_q)

#             if dist> distances[curr_vert]:
#                 continue

#             for neighbor,wt in self.adj_list[curr_vert]:
#                 distance = distances[curr_vert]+wt

#                 if distance<distances[neighbor]:
#                     distances[neighbor]=distance
#                     heapq.heappush((distance,neighbor))
#         return distances
# take inputs as no. of vertices, for loop (src,dest,wt), start vertex, print distances


    











