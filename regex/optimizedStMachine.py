# Title: FSM Optimization
# 
# Challenge Problem: 2 Stars
#
# Lexical analyzers are implemented using finite state machines generated
# from the regular expressions of token definition rules. The performance
# of a lexical analyzer can depend on the size of the resulting finite
# state machine. If the finite state machine will be used over and over
# again (e.g., to analyze every token on every web page you visit!), we
# would like it to be as small as possible (e.g., so that your webpages
# load quickly). However, correctness is more important than speed: even
# an optimized FSM must always produce the right answer.  
#
# One way to improve the performance of a finite state machine is to make
# it smaller by removing unreachable states. If such states are removed,
# the resulting FSM takes up less memory, which may make it load faster or
# fit better in a storage-constrained mobile device.
#
# For this assignment, you will write a procedure nfsmtrim that removes
# "dead" states from a non-deterministic finite state machine. A state is
# (transitively) "dead" if it is non-accepting and only non-accepting
# states are reachable from it. Such states are also called "trap" states:
# once entered, there is no escape. In this example FSM for r"a*" ...
#
# edges = { (1,'a') : [1] ,
#           (1,'b') : [2] ,
#           (2,'b') : [3] ,
#           (3,'b') : [4] } 
# accepting = [ 1 ] 
# 
# ... states 2, 3 and 4 are "dead": although you can transition from 1->2,
# 2->3 and 3->4 on "b", you are doomed to rejection if you do so. 
#
# You may assume that the starting state is always state 1. Your procedure
# nfsmtrim(edges,accepting) should return a tuple (new_edges,new_accepting)
# corresponding to a FSM that accepts exactly the same strings as the input
# FSM but that has all dead states removed. 

import copy

def nfsmtrim(edges, accepting): 
  visited = []
  keepers = []
  trimmers = []
  trimmedEdges = copy.deepcopy(edges)

  #find dead nodes/edges
  for node in edges:
    if nfsmHelper(node[0], edges, accepting, visited):
      keepers.append(node[0])

  keepSet = set(keepers)

  #remove unwanted edges
  for node in edges:
    for edge in edges[node]:
      if edge not in keepSet:
        trimmedEdges[node].remove(edge)

  #make list of unwanted nodes to pop
  for node in trimmedEdges:
    if len(trimmedEdges[node]) == 0:
      trimmers.append(node)

  #then pop 'em
  for node in trimmers:
    trimmedEdges.pop(node)

  return trimmedEdges, accepting


def nfsmHelper(current, edges, accepting, visited):
  if current in visited:
    return False
  elif current in accepting:
    return True
  else:
    #add current to visited
    newvisited = visited + [current]
    for node in edges:
      if node[0] == current:
        for edge in edges[node]:
          accepted = nfsmHelper(edge, edges, accepting, newvisited)
          if accepted:
            return True

# We have included a few test cases, but you will definitely want to make
# your own. 

edges1 = { (1,'a') : [1] ,
           (1,'b') : [2] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (8,'z') : [9] , } 
accepting1 = [ 1 ] 
(new_edges1, new_accepting1) = nfsmtrim(edges1,accepting1) 
print new_edges1
print new_edges1 == {(1, 'a'): [1]}
print new_accepting1 == [1] 

print "EDGES1 is"
print edges1

(new_edges2, new_accepting2) = nfsmtrim(edges1,[]) 
print new_edges2 == {}
print new_accepting2 == [] 

(new_edges3, new_accepting3) = nfsmtrim(edges1,[3,6]) 
print new_edges3
print new_edges3 == {(1, 'a'): [1], (1, 'b'): [2], (2, 'b'): [3]}
print new_accepting3 == [3]

edges4 = { (1,'a') : [1] ,
           (1,'b') : [2,5] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (3,'c') : [2,1,4] } 
accepting4 = [ 2 ] 
(new_edges4, new_accepting4) = nfsmtrim(edges4, accepting4) 
print new_edges4 == { 
  (1, 'a'): [1],
  (1, 'b'): [2], 
  (2, 'b'): [3], 
  (3, 'c'): [2, 1], 
}
#print new_edges4
print new_accepting4 == [2]
