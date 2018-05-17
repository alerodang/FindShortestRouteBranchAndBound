# Search methods

import search

a = "Lowest cost first:"
b = "Heuristic and cost lower sum first:"

ab = search.GPSProblem('A', 'B', search.romania)

oe = search.GPSProblem('O', 'E', search.romania)

so = search.GPSProblem('S', 'O', search.romania)

ln = search.GPSProblem('L', 'N', search.romania)

print("*** Search A -> B ***")
print a
print search.lowest_cost_first_graph_search(ab).path()
print b
print search.heuristic_first_graph_search(ab).path()

print("*** Search O -> E ***")
print a
print search.lowest_cost_first_graph_search(oe).path()
print b
print search.heuristic_first_graph_search(oe).path()

print("*** Search S -> O ***")
print a
print search.lowest_cost_first_graph_search(so).path()
print b
print search.heuristic_first_graph_search(so).path()

print("*** Search L -> N ***")
print a
print search.lowest_cost_first_graph_search(ln).path()
print b
print search.heuristic_first_graph_search(ln).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
