import random
import sys
import time
import numpy as np

def count(k):
    #This matrix is the something.
    matrix =[[2,3,4], [5,6,7],[44,45,46],[53,54,55],[8,9,10],[11,12,13],
        [14,15,16],[-1,-1,-1],[-1,-1,17],[-1,18,-1],[-1,-1,19],
        [-1,-1,20],[21,22,23],[-1,24,-1],[25,26,27],[-1,28,-1],[21,22,23],[25,26,27],[43,44,45],[47,-1,-1],
        [48,49,50],[51,-1,-1],[52,-1,-1],[66,67,68],[70,71,72],[73,-1,-1],[74,-1,-1],[76,-1,-1],[32,33,34],
        [35,36,37],[38,39,40],[-1,-1,41],[-1,-1,42],[43,44,45],[-1,-1,46],[-1,-1,-1],[47,-1,-1],
        [48,49,50],[51,-1,-1],[52,-1,-1],[-1,18,-1],[21,22,23],[-1,24,-1],[25,26,27],[-1,28,-1],
        [43,44,45],[48,49,50],[-1,65,-1],[66,67,68],[-1,69,-1],[70,71,72],[-1,73,-1],[56,57,58],
        [59,60,61],[62,63,64],[-1,65,-1],[66,67,68],[-1,69,-1],[70,71,72],[73,-1,-1],[74,-1,-1],
        [-1,75,-1],[76,-1,-1],[-1,-1,-1],[-1,-1,17],[-1,-1,19],[-1,-1,20],[21,22,23],[25,26,27],
        [-1,-1,41],[-1,-1,42],[43,44,45],[-1,-1,46],[48,49,50], [66,67,68], [70,71,72]]
    #This loop will initialize the transition matrix values to 0.
    transition = [[0 for r in range(len(matrix))] for c in range(len(matrix))]
    #This loop will increment the transition matrix where there
    #is a transition from a state of the matrix to another state.
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[0])):
            if(matrix[r][c] != -1):
                transition[r][matrix[r][c]-1] += 1
    #for i in transition:
    #    print i
    #Algorithm for determining to count strings of given length k
    #accepted by DFA.
    #Start vector with only the first state assigned to 1.
    #print len(transition)
    start = [0 for r in range(len(transition))]
    start[0] = 1
    #Accepting vector with all terminating states assigned to 1.
    accept = [[0 for r in range(0,1)] for c in range(0,len(transition))]
    for i in range(0, len(accept)):
        if((i > 15 and i < 28) or (i > 39 and i < 52) or (i > 64)):
            accept[i][0] = 1
    A = transition
    for r in range(0, k):
        A = np.dot(A, transition)
    return np.dot(np.dot(start,A), accept)
    
#main
if (__name__ == "__main__"):
    x = count(4)
    print x
#    for r in x:
#        print r
