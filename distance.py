def edit_distance(s1, s2):
    m=len(s1) + 1
    n=len(s2) +1
    operation =''

    tbl = {}
    for i in range(m):
        ## the insertition on the null string
        tbl[i,0]=i
    for j in range(n):
        ## the deletion on the null string
        tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):

            
            if s1[i-1]== s2[j-1]:
                cost = 0
                tbl[i,j] = (tbl[i-1, j-1]) 
##                operation = operation + 'c'
                
            else :
                cost = 1
                tbl[i,j] = (min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]) + cost)

    for i in range(m):
         for j in range(n):
            print tbl[i,j]
         print '------------'
       
    return tbl[i,j]

print(edit_distance("sunday", "saturday"))
