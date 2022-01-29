def MakeArrayConsecutive2(statues):
    statues.sort()
    count = 0;
    for i in range(max(statues)-min(statues)-1):
        if statues[i+1] != statues[i]+1:
            statues.insert(i+1, statues[i]+1)
            count += 1
    return count
