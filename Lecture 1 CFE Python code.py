# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 11:15:27 2022

@author: Hemant
"""

#%% Bond pricing

def bondprice(F,c,y,n):
    """price the cash flow of a bond
    using a single yield to maturity"""
    
    price = 0
    
    for i in range(1,n+1):
        
        if (i==n):
            cf = F + F*c*1
        else:
            cf = F*c*1
        
        price = price + cf/(1+y)**i
    
    return price

#%% Test function
# Test 1 is the function working
F = 100; c = 0.12; y = 0.05; n = 4;
p = bondprice(F,c,y,n)
print("bondprice:",p)
#%% Test function no discouting

F = 100; c = 0.12; y = 0.00; n = 4;
p = bondprice(F,c,y,n)
print("bondprice:",p)

#%% Test funcyion no coupon
F = 100; c = 0; y = 0.05; n = 4;
p = bondprice(F,c,y,n)
print("bondprice:",p)
print()

#%% test 4 coupon = yeild (par value)
F = 100; c = 0.12; y = c; n = 4;
p = bondprice(F,c,y,n)
print("bondprice:",p)


#%% Value of a bond with non integer time to maturity
def bondprice(F,c,y,T):
    
    price = 0
    t = T
    while(t>0):
        if (t == T):
            cf = F + F*c*1
        else:
            cf = F*c*1
        price = price + cf/(1+y)**t
        
        t = t-1
        
    return price


#%% Test function
# Test 1 is the function working
F = 100; c = 0.12; y = 0.05; T = 3.25;
p = bondprice(F,c,y,T)
print("bondprice:",p)
#%% Test function no discouting

F = 100; c = 0.12; y = 0.00; T = 4;
p = bondprice(F,c,y,T)
print("bondprice:",p)

#%% Test funcyion no coupon
F = 100; c = 0; y = 0.05; n = 4;
p = bondprice(F,c,y,n)
print("bondprice:",p)
print()

#%% test 4 coupon = yeild (par value)
F = 100; c = 0.12; y = c; n = 4;
p = bondprice(F,c,y,n)
print("bondprice:",p)



#%% bond yeld from price
def bondyield(F, c, n, P):
    """ find yield to match given price"""
    
    i = 0
    maxiter = 20
    eps = 0.0001
    # initial guess (yield =coupon )
    y = c
    while i<maxiter:
        
        print(F,c,y,n)
        p = bondprice(F,c,y,n)
        
        if abs(p-P) < eps:
            return y
        
        # estimating derivative
        p2 = bondprice(F, c, y+eps, n)
        
        #g(x) = bondprice(y) - p
        #x(i+1)= x(i) - g(x)/g'(x)
        
        y = y - (p-P)/ ((p2-p)/eps)
        
        i += 1 
        
    return "failed to converge"
        
#%% Test the yield price function

F=100; c =0.12; y = 0.05; n = 4;
p = bondprice(F,c,y,n)

impliedyield = bondyield(F, c, n, p)
print("yield", impliedyield)























