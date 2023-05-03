# this is a pathway challenge
# gotta get to the door at the end under a certain amount of time
# the hint is the bellman-ford algorithm: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
# reason:  the reason the belllmanford algorithm is being used is that algorithm helps each node calculate the distance from itself to 0, then to all other nodes to edges.  this way, from any particular node, you can see how far it is to the origin and the edges.
#  This is important to this problem, since the originating nodes: Start + bulkhead, are the most important ones, and hitting each row in any order can help sum up total travel time.  Then you can select the path that has the most coverage in the last amount of time, hitting each bunny as best as within the time constraints.

# a good explanation of the challenge can be found by this dev: https://github.com/aswintechguy?tab=repositories



# solution.solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)Output:    [0, 1]

# solution.solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)Output:    [1, 2]




def solution(times, times_limit):
    # solution requires bunnies so first get the number of bunnies
    total_bunnies = len(times) - 2
    bunnies = [x for x in range(1, total_bunnies)+1]
    
    # as stated in upper comments, bellmanford is designed to return distances from each node back to origin and edges, so we can determine optimum paths
    distances = calcBellmanFord(times)

    # logic quick, if you find a loop, then you can build infinite time and rescue all bunnies, so return the range of all bunnies
    if hasLoop(distances):
      return range(total_bunnies)