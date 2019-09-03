#Finding 2nd min element from the array
import math
#with O(n) time 
def fin2Min(a):
    m1=min(a[0],a[1])
    m2=max(a[0],a[1])
    for i in range(2,len(a)):
        if a[i]<m1:
            m1=a[i]
        elif a[i]<m2:
            m2=a[i]
        if m2==min(m1,m2):
            m1,m2=m2,m1
    return m2

def checkmin():
    a=list(map(int,input('Enter list of the array for 2ndMin ').split()))
    print(fin2Min(a))

#checkmin()

#first non repeating integer in an array
def nonRep(a):
    s=set()
    for i in a:
        if i not in s:
            s.add(i)
        else:
            s.remove(i)
    try:
        return next(iter(s))
    except StopIteration:
        return None

def CheckNonRep():
    a=list(map(int,input('Enter list of the array for NoneRep ').split()))
    result=nonRep(a)
    print('Every element is repeated atleast once') if result is None else print('number is ',result)

#CheckNonRep()

#Merge 2 sorted arrays
def mergeArray(a1,a2):#a1 with min length and a2 with max length
    result=[]
    i1=i2=0
    while True:
        if i1==len(a1) or i2==len(a2):
            break
        if a1[i1]<a2[i2]:
            result.append(a1[i1])
            i1+=1
        elif a1[i1]>a2[i1]:
            result.append(a2[i2])
            i2+=1
        else:
            result.append(a1[i1])
            result.append(a2[i2])
            i1+=1
            i2+=1
    
    if len(a1)==len(a2):
        if i1!=len(a1): result.append(a1[i1]);
        if i2!=len(a2): result.append(a2[i2]);
        return result
    else:
        result+=a1[len(a2):] if len(a1)>len(a2) else a2[len(a1):]
    return result
    
def CheckMergeArray():
    a1=list(map(int,input('Enter sorted array 1 ').split()))
    a2=list(map(int,input('Enter sorted array 2 ').split()))
    if len(a1)>len(a2):
        result=mergeArray(a2,a1)
    else:
        result=mergeArray(a1,a2)
    print(result)

#CheckMergeArray()


#Re-arrange +ve and -ve values in array
def arrngarr(a):
    return ([x for x in a if x<0]+[x for x in a if x>0])

def checkRearr():
    a=list(map(int,input('Enter sorted array 1 ').split()))
    print(arrngarr(a))

checkRearr()
