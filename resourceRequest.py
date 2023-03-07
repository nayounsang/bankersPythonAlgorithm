# inputs

T = 5  # num of thread
R = 3  # num of resourse
I = [10, 5, 7]  # instance
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
maxDemand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
available = [0] * R
need = [[0] * R for _ in range(T)]


def fillAvailable():
    # a = i - sum(allocation[t])
    for r in range(R):
        tmp = 0
        for t in range(T):
            tmp += allocation[t][r]
        available[r] = I[r] - tmp


def fillNeed():
    # n = m - a
    for t in range(T):
        for r in range(R):
            need[t][r] = maxDemand[t][r] - allocation[t][r]


def init():
    return [False] * T, list(available)


def isSmaller(a, b):
    # a <= b ?
    for v1, v2 in zip(a, b):
        if v1 <= v2:
            pass
        else:
            return False
    return True


def add(ref, tar):
    for i in range(R):
        ref[i] += tar[i]
    return ref


def sub(ref, tar):
    for i in range(R):
        ref[i] -= tar[i]
    return ref


fillAvailable()
fillNeed()
finish, work = init()

# request : thread t request instance of r
THREAD = 1  # who requests?
REQ = (1, 0, 2)  # what do thread requests?
if isSmaller(REQ, need[THREAD]):
    pass
else:
    raise ValueError
if isSmaller(REQ, available[THREAD]):
    pass
else:
    print('wait, not available')
    raise ValueError
available[THREAD] = list(sub(available[THREAD], REQ))
allocation[THREAD] = list(add(allocation[THREAD], REQ))
need[THREAD] = list(sub(need[THREAD], REQ))


#### and run safety, and make decide whether to reject ####
