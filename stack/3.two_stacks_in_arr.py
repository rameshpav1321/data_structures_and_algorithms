class TwoStack:
    def __init__(self,n) -> None:
        self.size=n
        self.arr=[None]*n 
        self.top1=-1
        self.top2=n
    def push1(self,x):
        # print('called p1', self.top1, self.top2)
        if self.top1<self.top2-1:
            self.top1+=1
            self.arr[self.top1]=x
        else:
            print("Stack Overflow!")

    def push2(self,x):
        # print('called p2', self.top1, self.top2)
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2]=x
        else:
            print("Stack Overflow!") 
    def pop1(self):
        if self.top1>=0:
            x=self.arr[self.top1]
            self.arr[self.top1]=None
            self.top1-=1
            return x
        else:
            print("Stack Underflow")
            return
    def pop2(self):
        if self.top2<self.size:
            x=self.arr[self.top2]
            self.arr[self.top2]=None
            self.top2+=1
            return x
        else:
            print("Stack Underflow")
            return

if __name__=="__main__":
    my_two_stack=TwoStack(6)
    my_two_stack.push1(1)
    my_two_stack.push2(1)
    my_two_stack.push1(2)
    my_two_stack.push2(2)
    my_two_stack.push1(3)
    my_two_stack.push2(3)
    print(my_two_stack.arr)
    print(my_two_stack.pop1())
    print(my_two_stack.pop2())
    print(my_two_stack.arr)
