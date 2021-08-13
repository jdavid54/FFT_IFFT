import numpy as np

# polynomials in coefficient representations
P0 = [0, 0, 1, 1]
P1 = [0,1,3]
P2 = [1,1,3]
P3 = [1]
P4 =[1,0,0,0,2]
P5 = [0,1]

# optimization
opt=True

def mul(P1,P2):
    ops=0
    l1 = len(P1)
    l2 = len(P2)
    y = [0]*(l1+l2-1)
    for m,i in enumerate(P2):
        if opt:
            if i!=0:
                for n,j in enumerate(P1):
                     if j!=0:
                        y[m+n] += i*j
                        ops+=1
        else:
             for n,j in enumerate(P1):
                        y[m+n] += i*j
                        ops+=1    
    print(P1,'*',P2,'=',y, ops,'ops instead of', l1*l2)
    # ops = product of numbers of elements not zero in 2 lists

mul(P1,P2)
mul(P1,P3)
mul(P2,P3)
mul(P4,P2)
mul(P2,P4)
mul(P1,P5)
mul(P0,P1)
mul(P1,P0)

def mul2(P1, P2):
    # convert to multiplication of integers and return in form of coefficient representation
    ops = 0
    p1 = [i*10**k for k,i in enumerate(P1) if i!=0]
    ops += len(p1)
    n1 = sum(p1)
    ops += len(p1)-1
    p2 = [i*10**k for k,i in enumerate(P2) if i!=0]
    ops += len(p2)
    n2 = sum(p2)
    ops += len(p2)-1
    #print(p1,p2)
    p = [int(i) for i in str(n1*n2)]
    p.reverse()    
    print(p, ops,'ops')
    return p


print()
mul2(P4,P2)
mul2(P2,P4)
mul2(P1,P5)
mul2(P0,P1)
mul2(P1,P0)