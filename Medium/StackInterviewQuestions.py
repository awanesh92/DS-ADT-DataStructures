class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __repr__(self):
##        return str(self.items)[1:-1]
        return ' '.join(str(i) for i in self.items)

#Solution for evaluating postfix expression
optrs=['+','-','/','*']
def EvalPostfix(a):
    st=Stack()
    for i in a:
        if i not in optrs:
            st.push(i)
        else:
            i1=str(st.pop())
            i2=str(st.pop())
            temp=str(i2+i+i1).replace('/','//')
            st.push(eval(temp))
    return st.pop()

def checkpostEval():
    a=input('Enter postfix expression')
    print(EvalPostfix(a))

#checkpostEval()


#solution for sorting values in stack
def sortstck(st):
    if not st.isEmpty():
        t=st.pop()
        sortstck(st)
        sortinsrt(st,t)
    return st

def sortinsrt(st,e):
    if st.isEmpty() or st.peek()<e:
        st.push(e)
    else:
        t=st.pop()
        sortinsrt(st,e)
        st.push(t)

def checksortstck():
    a=list(map(int,input('Enter stack elements').split()))
    st=Stack()
    for i in a:
        st.push(i)
    print(sortstck(st))

#checksortstck()


#solution for balanced paranthesis in Stack
openbracket=['(','{','[']
closebracket=[')','}',']']
def balparanth(a):
    st=Stack()
    for i in a:
        if i in openbracket:
            st.push(i)
        else:
            indx=openbracket.index(st.peek())
            if i==closebracket[indx]:
                st.pop()
            else:
                return False
    if st.isEmpty():
        return True
    else:
        return False

def chckbalparanth():
    a=input('Enter the paranthesis string to check if its balanced or not')
    if balparanth(a):
        print('Balanced Paranthesis')
    else:
        print('Un-Balanced Paranthesis')

chckbalparanth()
