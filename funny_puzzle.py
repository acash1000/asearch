import copy
import heapq

import numpy as np
import heapq as hq

tileplace = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1)}
goal = [1,2,3,4,5,6,7,8,0]

def manhattan(state):
    twodrep = get2d(state)
    man = 0
    for i in range(len(twodrep)):
        for j in range(len(twodrep[0])):
            neededval = tileplace.get(twodrep[i][j])
            current = (i, j)
            man += manhanttan_distance(current, neededval)
    return man

def manhanttan_distance(tile1, tile2):
    result = 0
    if(tile2 != None):
     result = abs(tile1[0] - tile2[0]) + abs(tile1[1] - tile2[1])
    return result

def goalstate(state):
    match = True
    for i in range(len(state[1])):
       if(state[1][i]!=goal[i]):
              match = False
    return match
def get2d(state):
    onedindex = 0
    twodrep = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            twodrep[i][j] = state[onedindex]
            onedindex += 1
    return twodrep


def indexOfZero(twod):
    for i in range(3):
        for j in range(3):
            if (twod[i][j] == 0):
                return (i, j)


def get1d(twod):
    oned = []
    for i in range(3):
        for j in range(3):
            oned.append(twod[i][j])
    return oned


def print_succ(state):
    two = get2d(state)
    izero, jzero = indexOfZero(two)
    lis = []
    for i in range(4):
        if (izero + 1 < 3 and i == 0):
            temp = copy.deepcopy(two)
            temptile = two[izero + 1][jzero]
            temp[izero][jzero] = temptile
            temp[izero + 1][jzero] = 0
            tempstate = get1d(temp)
            man = manhattan(tempstate)
            lis.append((tempstate, man))
        elif (izero - 1 >= 0 and i == 1):
            temp = copy.deepcopy(two)
            temptile = two[izero - 1][jzero]
            temp[izero][jzero] = temptile
            temp[izero - 1][jzero] = 0
            tempstate = get1d(temp)
            man = manhattan(tempstate)
            lis.append((tempstate, man))
        elif (jzero - 1 >= 0 and i == 2):
            temp = copy.deepcopy(two)
            temptile = two[izero][jzero - 1]
            temp[izero][jzero] = temptile
            temp[izero][jzero - 1] = 0
            tempstate = get1d(temp)
            man = manhattan(tempstate)
            lis.append((tempstate, man))
        elif (jzero + 1 < 3 and i == 3):
            temp = copy.deepcopy(two)
            temptile = two[izero][jzero + 1]
            temp[izero][jzero] = temptile
            temp[izero][jzero + 1] = 0
            tempstate = get1d(temp)
            man = manhattan(tempstate)
            lis.append((tempstate, man))
    lis = sorted(lis)
    for l in lis:
        print(repr(l[0])+ " h="+str(l[1]))

def getsuc(state):
    two = get2d(state)
    izero, jzero = indexOfZero(two)
    lis = []
    for i in range(4):
        if (izero + 1 < 3 and i == 0):
            temp = copy.deepcopy(two)
            temptile = two[izero + 1][jzero]
            temp[izero][jzero] = temptile
            temp[izero + 1][jzero] = 0
            tempstate = get1d(temp)
            man = manhattan(tempstate)
            lis.append((tempstate, man))
        elif (izero - 1 >= 0 and i == 1):
            temp = copy.deepcopy(two)
            temptile = two[izero - 1][jzero]
            temp[izero][jzero] = temptile
            temp[izero - 1][jzero] = 0
            tempstate = get1d(temp)
            man = manhattan(tempstate)
            lis.append((tempstate, man))
        elif (jzero - 1 >= 0 and i == 2):
            temp = copy.deepcopy(two)
            temptile = two[izero][jzero - 1]
            temp[izero][jzero] = temptile
            temp[izero][jzero - 1] = 0
            tempstate = get1d(temp)
            man = manhattan(tempstate)
            lis.append((tempstate, man))
        elif (jzero + 1 < 3 and i == 3):
            temp = copy.deepcopy(two)
            temptile = two[izero][jzero + 1]
            temp[izero][jzero] = temptile
            temp[izero][jzero + 1] = 0
            tempstate = get1d(temp)
            man = manhattan(tempstate)
            lis.append((tempstate, man))
    lis = sorted(lis)
    return lis
def complist(l1,l2):
    match = True
    for i in range(len(l1)):
        if (l1[i] != l2[i]):
            match = False
    return match

def getlist(tracked,firstparent,last):
    parent = firstparent
    solution = []
    solution.append(last)
    parentstate = last[2][3]
    while parent !=-1:
        for s in tracked:
            if s[2][0] == parent:
                if(complist(parentstate,s[1])):
                    solution.append(s)
                    parent = s[2][2]
                    if(parent!=-1):
                     parentstate = s[2][3]
                    break
    return solution
def solve(state):
    open = []
    tracked = []
    close = []
    h = manhattan(state)
    heapq.heappush(open,(h,state,(0,h,-1)))
    best = None
    bestpath = None
    bestmove = 1000
    while len(open)>0:
       current = heapq.heappop(open)
       move = current[2][0] +1
       if(current[1] in tracked):
            continue
       else:
            tracked.append(current[1])
            close.append(current)
       if(goalstate(current)):
         f = current[2][0] +current[2][1]
         if best == None or f < (best[2][0] + best[2][1]):
             li = getlist(close,current[2][2],current)
             bestpath = li
             best = current
             break;
       else:
         suc = getsuc(current[1])
         for s in suc:
            h = s[1]
            f = h+move
            heapq.heappush(open,(f,s[0],(move,s[1],current[2][0],current[1])))
    bestpath.reverse()
    for entry in bestpath:
        print(repr(entry[1]) + " h=" + str(entry[2][1]) + " moves: " + str(entry[2][0]))

# 1,2,3
# 4,5,0
# 6,7,8

# 1, 2, 0,
# 4, 5, 3,
# 6, 7, 8

# 1, 2, 3,
# 4, 0, 5
# 6, 7, 8

# 1, 2, 3,
# 4, 5, 8,
# 6, 7, 0
