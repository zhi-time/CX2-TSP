def indexOf(arr, x):
    for a in range(len(arr)):
        if arr[a] == x:
            return a
    return -1

def findUnusedIndexValues(parent, offspring,st):
    for i in range(len(parent)):
        if parent[i] in offspring:
            st[i]=0
    res = []
    for i in range(len(parent)):
        if st[i] == 1:
            res.append(parent[i])
    return res,st



def crossoverOperator2(parent1, parent2,st1,st2):# st1和st2是和parent1以及parent2等长的全为1的数组
    num1 =0
    num2 = 0
    start1=-1
    start2=-1
    for i in range(len(st1)):
        if(st1[i]==1):
            num1+=1
            if(start1==-1):
                start1=i

    for i in range(len(st2)):
        if(st2[i]==1):
            num2+=1
            if(start2==-1):
                start2=i

    offspring1 = [None] * num1
    offspring2 = [None] * num2
    if start1==-1 and start2 == -1:
        return [],[]

    i1 = 0
    i2 = 0
    initialSelected = parent1[start1]
    offspring1[i1] = parent2[start2]
    i1 += 1
    check = 1

    while i1 < num1 and i2 < num2:
        index1 = indexOf(parent1, offspring1[i1 - 1])
        index1 = indexOf(parent1, parent2[index1])
        latestUpdated2 = parent2[index1]
        if latestUpdated2 == initialSelected:
            offspring2[i2] = latestUpdated2
            i2 += 1
            check = 0
            res1,st1= findUnusedIndexValues(parent1, offspring2,st1)
            res2,st2= findUnusedIndexValues(parent2, offspring1,st2)
            ans1, ans2 = crossoverOperator2(parent1, parent2,st1,st2)
            offspring1[i1:] = ans1
            offspring2[i2:] = ans2
            check = 0
            break
        else:
            offspring2[i2] = parent2[index1]
            i2 += 1
            index1 = indexOf(parent1, offspring2[i2 - 1])
            offspring1[i1] = parent2[index1]
            i1 += 1
    if check:
        index1 = indexOf(parent1, offspring1[i1 - 1])
        index1 = indexOf(parent1, parent2[index1])
        latestUpdated2 = parent2[index1]
        offspring2[i2] = latestUpdated2
        i2 += 1
    return offspring1, offspring2
