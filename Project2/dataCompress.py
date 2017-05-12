#!/usr/bin/env python
# Fern Vue
# Lisa Churchman

import pygtrie as pygtrie
import itertools
import time

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
    if(k >20):
        return["".join(seq) for seq in itertools.product("01", repeat=5)]
    return["".join(seq) for seq in itertools.product("01", repeat=k)]

def getPrefixes(w):
    pre = [w[0:len(w)-i] for i in range(0,len(w))]
    return pre[::-1]

def buildAD(trie, k):
    allPossible = []
    count = 0
    for i in range (1,k):
        possible = allPossibleStrings(i)
        for pos in possible:
            allPossible.append(pos)
    adTrie = pygtrie.CharTrie()
    for word in allPossible:
        if not trie.has_key(word):
            possible = getPrefixes(word)
            flag = False
            for pos in possible:
                if adTrie.has_key(pos):
                    flag = True
                    count = count + 1
                    break
                if (count > 1000000):
                    break
            if(not flag):
                adTrie[word] = True
        if (count > 1000000):
            break
    return adTrie

def getSuffixes(w):
    return [w[i:] for i in range(1,len(w))]


def encoder(AD, w):
    v = ""
    r = ""
    for c in w:
        suffixes = getSuffixes(v)
        flag = False
        for s in suffixes:
            if(AD.has_key(s + "0") or (AD.has_key(s+"1"))):
                flag = True
        if(not flag):
            r = r + c
        v = v + c
    return(len(w), r)

def decoder(AD, w, n):
    v = ""
    count = 0
    while(len(v) < n):
        suffixes = getSuffixes(v)
        flag = False
        for s in suffixes:
            if(AD.has_key(s + "0")):
                v = v + "1"
                flag = True
                break
            elif(AD.has_key(s+"1")):
                v = v + "0"
                flag = True
                break
        if (not flag):
            b = w[count]
            v = v + b
            count = count + 1
        flag = False
    return v

def encodeNdecode(w):

    print "Input String:", w
    print "Length of input string:", len(w)
    buildTime = time.time()
    AD = buildAD(buildFact(w),len(w))
    afterBuild = time.time()
    print "Time to build anti dictionary:",afterBuild - buildTime

    encodeTime = time.time()
    v,r = encoder(AD,w)
    endTime = time.time()
    print "Time to encode:", endTime - encodeTime
    print "Encoded String:", r
    print "Length of encoded string:", len(r)

    decodeTime = time.time()
    d = decoder(AD, r, v)
    endTime = time.time()
    print "Time to decode:", endTime - decodeTime
    print "Decoded String:", d

    if(w == d):
        print "The decoded string and input string are equal"
    else:
        print "The decoded string and input string are NOT equal"
    print

w = '01001010'
x = '01001101000'
y = '1010011001010100001010100110010101000010101001100101010000101010011001010100001010100110010101000010'
z='00100110010101010101100101110100110010101000010101001100101010000101010011001010100001010100110010101000010101001100101010000100001001100101010101011001011101001100101010000101010011001010100001010100110010101000010101001100101010000101010011001010100001000010011001010101010110010111010011001010100001010100110010101000010101001100101010000101010011001010100001010100110010101000010000100110010101010101100101110100110010101000010101001100101010000'
encodeNdecode(w)
encodeNdecode(x)
encodeNdecode(y)
encodeNdecode(z)
