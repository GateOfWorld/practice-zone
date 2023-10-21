import random as R

def Qsort(slist:list, start:int=0, end:int=-1)->None:
    if end==-1: end = slist.__len__()
    if slist[start:end].__len__()<=1 : return
    elif slist[start:end].__len__()==2:
        if slist[start]>slist[start+1]:slist[start],slist[start+1]=slist[start+1],slist[start]
        return
    pivot = slist[start]
    
def Msort(slist:list, start:int=0, end:int=-1)->None:
    if end==-1 : end=slist.__len__()
    if slist[start:end].__len__()<=1 : return
    elif slist[start:end].__len__()==2:
        if slist[start]>slist[start+1]:slist[start],slist[start+1]=slist[start+1],slist[start]
        return
    Msort(slist, start,(start+end)//2)
    Msort(slist, (start+end)//2, end)
    p1, p2 = start, (start+end)//2
    while(p1!=p2)and(p2!=end):
        if slist[p1]>slist[p2] :
            slist.insert(p1,slist.pop(p2))
            p2+=1
        p1+=1
    return

if __name__=="__main__" :
    l=[]
    for _ in range(10):l.append(R.randint(0,100))
    Msort(l)
    print(l)