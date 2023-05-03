# this is a pathway challenge
# gotta get to the door at the end under a certain amount of time
# the hint is the bellman-ford algorithm: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
# reason:  the reason the belllmanford algorithm is being used is that algorithm helps each node calculate the distance from itself to 0, then to all other nodes to edges.  this way, from any particular node, you can see how far it is to the origin and the edges.
#  This is important to this problem, since the originating nodes: Start + bulkhead, are the most important ones, and hitting each row in any order can help sum up total travel time.  Then you can select the path that has the most coverage in the last amount of time, hitting each bunny as best as within the time constraints.

# a good explanation of the challenge can be found by this dev: https://github.com/aswintechguy?tab=repositories



# solution.solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)Output:    [0, 1]

# solution.solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)Output:    [1, 2]



from itertools import permutations

######### BEGINNING BELLMANFORD IMPLEMENTATION ##########
## This is slightly different than normal bellman ford because this approach
## hits all the vertex

def findDistance(graph, source):
    n = len(graph)
    distance = [float('inf')] * len(graph) #the assumption is infinite based on start
    # now initialize the source
    distance[source] = 0

    # continue bellman ford and iterate throught the vertices
    for i in range(n):
        for j in range(n):
            for k in range(n):
                weight = graph[j][k]
                # now verify the first condition
                # and if a path is found that's more efficient, then update the distance
                if distance[j] + weight < distance[k]:
                    distance[k] = distance[j] + weight
    return distance


def calcBellmanFord(graph):
    distances = []
    for vert in range(len(graph)):
        distances.append(findDistance(graph, vert))
    return distances
######### END OF BELLMANFORD IMPLEMENTATION########

def hasLoop(graph):
    distance = graph[0]
    n = len(graph)
    for j in range(n):
            for k in range(n):
                weight = graph[j][k]
                if distance[j] + weight < distance[k]:
                    # then a loop has been found
                    return True
    return False

def getStepsAndTime(bunnies, graph):
    # total time can be started with the first path found
    # bunnies[0] transition bunny at the start
    totalTime = graph[0][bunnies[0]]
    # now add the time to get to the bulkhead
    # bunnies[-1] transition bunny right before bulkhead
    totalTime += graph[bunnies[-1]][len(graph)-1]
    for i in range(1, len(bunnies)):
        # starting bunny
        u = bunnies[i-1]
        # ending bunny
        v = bunnies[i]
        # now add the total time from 'u' bunny to 'v' bunny
        totalTime += graph[u][v]
    return totalTime

def solution(times, times_limit):
    # solution requires bunnies so first get the number of bunnies
    total_bunnies = len(times) - 2
    bunnies = [x for x in range(1, total_bunnies)]
    
    # as stated in upper comments, bellmanford is designed to return distances from each node back to origin and edges, so we can determine optimum paths
    distances = calcBellmanFord(times)

    # logic quick, if you find a loop, then you can build infinite time and rescue all bunnies, so return the range of all bunnies
    if hasLoop(distances):
      return range(total_bunnies)
    
    # now iterate through permutations, so that you can find the best path with as many bunnies as possible saved
    for i in range(total_bunnies, 0, -1):
        # using permutations, it'll automatically calculate and try the different iterations in the combination of total bunny indexes in 'bunnies' + to the index indicated in the range of (total_bunnies)
        for eachPerm in permutations(bunnies, i):
            # now calculate the total time based on the steps
            totalTime = getStepsAndTime(eachPerm, distances)
            if totalTime <= times_limit:
                return [x-1 for x in sorted(eachPerm)]
    
    # just in case nothing is possible
    return []