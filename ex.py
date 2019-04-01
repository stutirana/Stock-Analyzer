def max_diagonal(L:[[int]]):
    count=1
    li=[]
    for i in range(len(L)-1):
        if i>0 and start_cell == L[i][i]:
            count+=1
        elif i==0:
            start_cell=L[i][i]
        else:
            li.append(count)
            count=1
            start_cell=L[i][i]
    if max(li) == 1:
        return 0
    else:
        return max(li)
