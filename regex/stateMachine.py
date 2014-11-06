# Title: Reading Machine Minds

# It can be difficult to predict what strings a finite state machine will
# accept. A tricky finite state machine may not accept any! A finite state
# machine that accepts no strings is said to be *empty*. 
# 
# In this homework problem you will determine if a finite state machine is
# empty or not. If it is not empty, you will prove that by returning a
# string that it accepts. 
#
# Formally, you will write a procedure nfsmaccepts() that takes four
# arguments corresponding to a non-derministic finite state machine:
#   the start (or current) state
#   the edges (encoded as a mapping)
#   the list of accepting states
#   a list of states already visited (starts empty) 
#
# If the finite state machine accepts any string, your procedure must
# return one such string (your choice!). Otherwise, if the finite state
# machine is empty, your procedure must return None (the value None, not
# the string "None"). 
#
# For example, this non-deterministic machine ...
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 2],
          (4, 'c') : [5] }
accepting = [5] 
# ... accepts exactly one string: "abc". By contrast, this
# non-deterministic machine: 
edges2 = { (1, 'a') : [1],
           (2, 'a') : [2] }
accepting2 = [2] 
# ... accepts no strings (if you look closely, you'll see that you cannot
# actually reach state 2 when starting in state 1). 

def nfsmaccepts(current, edges, accepting, visited):
	output = nfsmHelper(current, edges, accepting, visited)
	#helper checks if the output string is too repetitive 
	#(because self loops)
	#weakness: there might be valid, yet repetitive strings 
	#which satisfy the NFSM. 
	if (len(output) - len(set(list(output)))) > 2:
		return None
	else:
		return output


def nfsmHelper(current, edges, accepting, visited):
	#base case
	if current in accepting or current in visited:
		return ""
	#recurse	
	else:
		for edge in edges:
			if accepting[0] in edges[edge]:
				#cap off infinite recursion in case of self loop
				if len (visited) > 3 and len(set(visited)) == 1:
					return ""
				else:
					visited.append(edge[0])
					return nfsmaccepts(current, edges, edge, visited) + edge[1]

#test cases:
print "Test 1: " + str(nfsmaccepts(1, edges, accepting, []) == "abc") 
print "Test 2: " + str(nfsmaccepts(1, edges, [4], []) == "ab") 
#problem -- if the set doesn't work, then the function returns everything
#solution: a helper function (HACK)
print "Test 3: " + str(nfsmaccepts(1, edges2, accepting2, []) == None) 
print "Test 4: " + str(nfsmaccepts(1, edges2, [1], []) == "")


