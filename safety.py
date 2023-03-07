# inputs
T = 5 # num of thread
R = 3 # num of resourse
I = [10,5,7] # instance
allocation = [
    [0,1,0],
    [2,0,0],
    [3,0,2],
    [2,1,1],
    [0,0,2]
    ]
maxDemand = [
    [7,5,3],
    [3,2,2],
    [9,0,2],
    [2,2,2],
    [4,3,3]
    ]
available = [0]*R
need = [[0]*R for _ in range(T)]


def fillAvailable():
    for r in range(R):
        tmp = 0
        for t in range(T):
            tmp += allocation[t][r]
        available[r] = I[r] - tmp

        
def fillNeed():
    for t in range(T):
        for r in range(R):
            need[t][r] = maxDemand[t][r] - allocation[t][r]


def init():
    # t: num of thread
    return [False] * T, list(available)


def isSmaller(t):
    for n,w in zip(need[t],work):
        if n <= w:
            pass
        else:
            return False
    return True


def addWork(t):
    for w in range(R):
        work[w] += allocation[t][w]


fillAvailable()
fillNeed()
finish,work = init()
seq = []
while True:
    change = False
    for t in range(T):
        if finish[t]:
            continue
        if isSmaller(t):
            seq.append(t)
            addWork(t)
            finish[t] = True
            change = True
    if not change:
        break
print(*seq)
