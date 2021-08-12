import numpy as np
exp = np.exp
pi = np.pi
P = [1, 2, 0, 6, 1, 0, 0, 0]   # y = 1 + 2x + 6x**3 + x**4
P = [0, 0, 1, 0]  # y = x**2
debug = False

def FFT(P):
    # P is a polynomial with [p0,p1,...p(n-1)] as coeff representation
    n = len(P)  # n is a power of 2
    print('n :',n)
    if n==1:
        return P
    w = exp(2*pi*1j/n)
    #Pe = [p for i,p in enumerate(P) if i%2==0]
    #Po = [p for i,p in enumerate(P) if i%2==1]
    Pe, Po = P[::2], P[1::2]
    ye, yo = FFT(Pe), FFT(Po)
    
    y = [0]*n
    
    for j in range(int(n/2)):
        y[j] = ye[j] + w**j*yo[j]
        y[j+int(n/2)] = ye[j] - w**j*yo[j]
        print(j,'y =', y)
    if debug:
        print('w:',w)
        print('Pe :',Pe,',Po :',Po)
        print('ye :',ye,'\nyo :',yo,'\n')
    return y
 
fft = FFT(P) 
print('FFT(P) =', fft, len(fft))


def IFFT(P):
    # P is a polynomial with [P(w**0),P(w**1),...,P(w**n-1)] as value representation
    n = len(P)
    print('n :',n)
    if n == 1: # base case
        return P
    w = 1/n*exp(-2*pi*1j/n)
    Pe, Po = P[::2], P[1::2]
    ye, yo = IFFT(Pe), IFFT(Po)
    
    y = [0]*n
    for j in range(int(n/2)):
        y[j] = ye[j] + w**j*yo[j]
        y[j+int(n/2)] = ye[j] - w**j*yo[j]
    if debug:
        print('n:',n,',w:',w)
        print('Pe:',Pe,',Po:',Po)
        print('ye:',ye,'\nyo:',yo,'\n')
    return y

ifft = IFFT(fft)
print('IFFT =', ifft, len(ifft))
print('IFFT(P)=',[v.real for v in ifft])
