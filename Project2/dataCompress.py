#!/usr/bin/env python
# Fern Vue
# Lisa Churchman

import pygtrie as pygtrie
import itertools

def buildFact(w):
    trie = pygtrie.CharTrie()
    words = allSubstrings(w)
    for word in words:
        trie[word] = True 
    return trie

def allSubstrings(w):
    j=1
    a=set()
    while True:
        for i in range(len(w)-j+1):
            a.add(w[i:i+j])
        if j==len(w):
            break
        j+=1
    return list(a)

def allPossibleStrings(k):
    return["".join(seq) for seq in itertools.product("01", repeat=k)]

def buildAD(trie, k):
    allPossible = []
    for i in range (1,5):
        possible = allPossibleStrings(i)
        for pos in possible:
            allPossible.append(pos)
    adTrie = pygtrie.CharTrie()
    for word in allPossible:
        if not trie.has_key(word):
            possible = allSubstrings(word)
            for pos in possible:
                if not adTrie.has_subtrie(pos):
                    adTrie[word] = True
                else:
                    break;
    return adTrie

def encoder(AD, w):
    v,r = ""
    for char in w:
        


print buildAD(buildFact('10010') ,5)
