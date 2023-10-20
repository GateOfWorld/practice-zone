import random as R

def Qsort(slist:list)->list:
    if(len(slist)<=1):
        return slist
    else:
        pivot = slist[0]
        low = [x for x in slist[1:] if x < pivot]
        large = [x for x in slist[1:] if x >= pivot]
        if low.__len__()>1 : low = Qsort(low) 
        if large.__len__()>1 : large = Qsort(large)
        return low + [pivot] + large

def Bsort(arr:list):
    for front_index in range(0, len(arr) - 1):
        for index in range(front_index + 1, len(arr)):
            if arr[front_index]>arr[index]:
                arr[front_index],arr[index]=arr[index],arr[front_index]

def Msort(slist:list, start, end)->list:
    list1=slist[0:int(len(slist)/2)]
    list2=slist[int(len(slist)/2):len(slist)]
    if(len(list1)>1):list1=Msort(list1)
    if(len(list2)>1):list2=Msort(list2)
    reslist = []
    while(len(list1)>0)and(len(list2)>0):
        reslist.append(list1.pop(0)if list1[0]<list2[0]else list2.pop(0))
    if(len(list1)>0):reslist.extend(list1)
    else:reslist.extend(list2)
    return reslist

if __name__=="__main__" :
    l=[]
    for _ in range(1000):l.append(R.randint(0,65535))
    print(1)
    print(Qsort(l))
    Bsort(l)
    print(l)