class node:
    def __init__(self, data:any) -> None:
        self.data = data
        self.next = None
    
class stack:
    def __init__(self) -> None:
        self.top = None
        self.count = 0
    
    def push(self,n:node)->None:
        n.next=self.top
        self.top=n
        self.count+=1
    
    def pop(self)->node:
        if self.count<1:
            return None
        else:
            res:node =  self.top
            self.top = self.top.next
            self.count-=1
            res.next = None
            return res

if __name__=="__main__":
    s = stack()
    cmd:str = None
    while cmd!="shutdown":
        cmd=str(input("command\n1:push\t\t2:pop"))
        if cmd=="1":
            s.push(node(input("data?")))
        elif cmd=="2":
            tmp=s.pop()
            if tmp!=None:
                print(tmp.data)
            else : print("empty!!")