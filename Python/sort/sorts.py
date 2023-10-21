def listswap(slist:list, a:int, b:int|None=None):
    """리스트 내 두 인덱스의 데이터를 교환합니다."""
    if b == None : b = a+1
    slist[a],slist[b] = slist[b],slist[a]

def Qsort(slist:list, start:int=0, end:int|None=None)->None:
    """퀵정렬을 실행합니다."""
    if end == None : end = slist.__len__()
    if slist[start:end].__len__() <= 2 : 
        if (slist[start:end].__len__() == 2) and (slist[start] > slist[start+1]) : 
            listswap(slist, start)
        return
    pivot = start
    for i in range(start, end-1) :
        if slist[i] <= slist[end-1] :
            if i!=pivot : listswap(slist,pivot,i)
            pivot+=1
    listswap(slist, pivot, end-1)
    Qsort(slist, start, pivot)
    Qsort(slist, pivot, end)
    
def Msort(slist:list, start:int=0, end:int|None=None)->None:
    """머지정렬을 실행합니다."""
    if end == None : end=slist.__len__()
    if slist[start:end].__len__() <= 2 :
        if (slist[start:end].__len__() == 2) and (slist[start] > slist[start+1]) : 
            listswap(slist, start)
        return
    Msort(slist, start,(start+end)//2)
    Msort(slist, (start+end)//2, end)
    p1, p2 = start, (start+end)//2
    while (p1!=p2)and(p2!=end) :
        if slist[p1] > slist[p2] :
            slist.insert(p1,slist.pop(p2))
            p2+=1
        p1+=1
    return

def Bsort(slist:list):
    """버블정렬 \n 
    slist : 리스트"""
    for i in range(0,len(slist)) :
        for j in range (i,len(slist)) :
            if slist[i] > slist[j] : listswap(slist, i, j)



if __name__=="__main__" :
    import random as R
    l=[]
    #c=R.randint(0,490)
    for _ in range(60000) : l.append(R.randint(0,65536))
    #Bsort(l)
    #print(l[c:c+10]+[l[-1],l[0]])
    #R.shuffle(l)
    #print(l)
    Msort(l)
    #print(l[c:c+10]+[l[-1], l[0]])
    R.shuffle(l)
    #print(l)
    Qsort(l)
    #print(l[c:c+10]+[l[-1], l[0]])
    R.shuffle(l)