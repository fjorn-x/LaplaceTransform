from math import factorial,pow

def constant(a,b) :
    num=str(a)
    den="s"
    return num,den;

def expo(a,b) :
    
    num=str(a*1) 
    
    c=abs(b)
    if b<=0 :
        den="s + " + str(c)
    else :
        den="s - " +str(c)

    return num,den;
    

def tfunc(constant,b) :
    fact=int(factorial(b))
    num=str(fact*constant)
    den='s^'+str(b+1)
    return num,den

def sine(a,b) :
    num=str(a*b)
    den="s^2 + " + str(int(pow(b,2)))
    return num,den

def cos(a,b) :
    num=str(a*b)+"s"
    den="s^2 + " + str(int(pow(b,2)))
    return num,den

def expo_sin(a, b): 
    num=str(b)
    c=abs(a)
    if a<=0:
        den='(s + ' + str(c) + ')^2 + '+str(int(pow(b,2))) 
    else:
        den='(s - ' + str(c) + ')^2 + '+str(int(pow(b,2))) 
    return num,den

def expo_cos(a, b): 
    
    c=abs(a)
    if a<=0 :
        num='s + ' +str(c)
        den='(s + ' + str(c) + ')^2 + '+str(int(pow(b,2)))
    else:
        num='s - ' +str(c)
        den='(s - ' + str(c) + ')^2 + '+str(int(pow(b,2)))
    return num,den

def expo_sinh(a, b): 
    num=str(b)
    c=abs(a)
    if a<=0:
        den='(s + ' + str(c) + ')^2 '+' - '+str(int(pow(b,2)))
    else:
        den='(s - ' + str(c) + ')^2 '+' - '+str(int(pow(b,2)))
    return  num,den

def expo_cosh(a, b): 
    c=abs(a)
    if a<=0 :
        num='s + '+str(c)
        den='(s + ' + str(c) + ')^2 - '+str(int(pow(b,2))) 
    else:
        num='s - '+str(c)
        den='(s - ' + str(c) + ')^2 - '+str(int(pow(b,2))) 
    return num,den

def t_expo(n,a) :
    num=str(int(factorial(n)))
    c=abs(a)
    if a<=0 :
        den='(s + ' + str(c) +')^' +str(n+1)
    else:
        den='(s - ' + str(c) +')^' +str(n+1)
    return  num,den

def sinh(a,b) :
    num=str(int(a*b))
    den='s^2 - '+str(int(pow(b,2)))
    return num,den


def cosh(a,b) :
    num=str(a)+'s'
    den='(s^2 - '+str(int(pow(b,2)))+')'
    return num,den
