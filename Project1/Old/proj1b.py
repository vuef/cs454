import random
import sys
import time
import numpy as np

'''
    Function for determining the number of strings of 
    a given length k accepted by DFA.
    Language: Any substring of length 4, all three
    letters a,b and c occur.
'''

def count(k):
    #This matrix is the DFA. Sorted by 5's
    matrix = [[1,2,3], [4,5,6], [28,29,30], [52,53,54], [7,8,9], 
            [10,11,12],[13,14,15],[-1,-1,-1],[-1,-1,16],[-1,17,-1],
            [-1,-1,18],[-1,-1,19],[20,21,22],[-1,23,-1],[24,25,26],
            [-1,27,-1],[20,21,22],[24,25,26],[42,43,44],[46,-1,-1],
            [47,48,49],[50,-1,-1],[51,-1,-1],[65,66,67],[69,70,71],
            [72,-1,-1],[73,-1,-1],[75,-1,-1],[31,32,33],[34,35,36],
            [37,38,39],[-1,-1,40],[-1,-1,41],[42,43,44],[-1,-1,45],
            [-1,-1,-1],[46,-1,-1],[47,48,49],[50,-1,-1],[51,-1,-1],
            [-1,17,-1],[20,21,22],[-1,23,-1],[24,25,26],[-1,27,-1],
            [42,43,44],[47,48,49],[-1,64,-1],[65,66,67],[-1,68,-1],
            [69,70,71],[-1,74,-1],[55,56,57],[58,59,60],[61,62,63],
            [-1,64,-1],[65,66,67],[-1,68,-1],[69,70,71],[72,-1,-1],
            [73,-1,-1],[-1,74,-1],[75,-1,-1],[-1,-1,-1],[-1,-1,16],
            [-1,-1,18],[-1,-1,19],[20,21,22],[24,25,26],[-1,-1,40],
            [-1,-1,41],[42,43,44],[-1,-1,45],[47,48,49],[65,66,67],
            [69,70,71]]
    #This loop will initialize the transition matrix (76x76) values to 0. 
    transition = [[0 for r in range(len(matrix))] for c in range(len(matrix))]
    #This loop will increment the transition matrix where there
    #is a transition from a state of the matrix to another state.
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[0])):
            if(matrix[r][c] != -1):
                transition[r][matrix[r][c]] += 1
    # Start vector (1x76) with only the first state assigned to 1.
    start = [0 for r in range(len(transition))]
    start[0] = 1
    #Accepting vector (76x1) with all terminating states assigned to 1.
    accept = [[0 for r in range(0,1)] for c in range(0,len(transition))]
    for i in range(0, len(accept)):
        if((i > 15 and i < 28) or (i > 39 and i < 52) or (i > 63)):
            accept[i][0] = 1
    '''Matrix Formula A^k'''
    A = transition
    for r in range(1, k):
        A = np.dot(A,transition)
    '''uA^kv'''
    return np.dot(np.dot(start,A), accept)[0]

'''
    Function that outputs a string of the shortest length
    (lexicographically first in case of more than one string)
    accepted by the DFA. This function will call findInt
    in order to find the smallest multiple of a number x 
    consisting only a specified subset s of the DFA alphabet.
'''
def minString(x, s):
    visited = [0 for v in range(x)]
    transition = [-1]*x
    parent = [-1]*x
    queue = [0]
    flag = True
    while queue and flag:
        r = queue.pop(0)
        for y in s:
            nextInt = findInt(r,x,y)
            if(visited[nextInt] == 0):
                parent[nextInt] = r
                visited[nextInt] = 1
                transition[nextInt] = y
                queue.append(nextInt)
                if(nextInt == 0):
                    flag = False
                    break
    if not queue:
        return -1
    l = ''
    current = 0
    l += str(transition[current])
    current = parent[current]
    while(current != 0):
        l += str(transition[current])
        current = parent[current]
    return l[::-1]

'''
    Returns the next index.
'''
def findInt(r,x,s):
    return (r * 10 + s) % x

#    Function that takes an input string w and outputs a
#    regular expression R such that L(R) includes all strings
#    that are at edit distance 1 from w. A word s is said to be at
#    distance 1 from w if performing only one of the operations listed
#    on s results in w:
#        a) replace one letter of s by an arbitrary letter
#        b) delete a letter of s
#        c) insert a new letter in any position of s
#    EXAMPLE: dg, dogr, dag are all at distance 1 from dog.
#            But god, dagr etc. are not at distance 1 from dog.
#
def regular(w):
    # w + 1 inserts
    # w deletions
    # w replacements
    # Insert = do the rest.
    # Delete = e do the rest.
    # replace = do the rest.
    return 0
#main
if (__name__ == "__main__"):
    while True:
        i = raw_input("1.count 2.minString 3.regularExpression q.Quit\nEnter a problem number to test: ")
        if(i == "q"):
            break;
        if(int(i) == 1):
            v = input("This test will return the number of strings of length n\nEnter a number n: ")
            print count (v)
        if(int(i) == 2):
            b = (raw_input("This test will output a integer of the shortest length of a\nmultiple of a given number consisting of a subset of the alphabet [0-9].\nInput: <number> <subSet[0-9]> (set is space delimited): "))
            v = [int(x) for x in b.split()]
            print minString(v[0], v[1:])
        if(int(i) == 3):
            v = input("Output: A regular expression that includes all strings\nthat are at edit distance 1 from the the given string.\nEnter an input string: ")
            print v
        print
