import math

def constant(a,b) :
    num=str(a)
    den="s"
    return num,den;

def expo(a,b) :
    
    num=str(a*1) 
    #den="s - " + str(b)
    c=-abs(b)
    if b<=0 :
        den="s + " + str(c)
    else :
        den="s - " +str(c)

    return num,den;
    

def tfunc(constant,b) :
    fact=int(math.factorial(b))
    num=str(fact*constant)
    den='s^'+str(b+1)
    return num,den

def sine(a,b) :
    num=str(a*b)
    den="s^2 + " + str(int(math.pow(b,2)))
    return num,den

def cos(a,b) :
    num=str(a*b)+"s"
    den="s^2 + " + str(int(math.pow(b,2)))
    return num,den

def expo_sin(a, b): 
    num=str(b)
    den='(s - ' + str(a) + ')^2 + '+str(int(math.pow(b,2))) 
    return num,den

def expo_cos(a, b): 
    num='s - ' +str(a)
    den='(s - ' + str(a) + ')^2 + '+str(int(math.pow(b,2)))
    return num,den

def expo_sinh(a, b): 
    num=str(b)
    den='(s - ' + str(a) + ')^2 - '+str(int(math.pow(b,2)))
    return  num,den

def expo_cosh(a, b): 
    num='s - '+str(a)
    den='(s - ' + str(a) + ')^2 - '+str(int(math.pow(b,2))) 
    return num,den

def t_expo(n,a) :
    num=str(int(math.factorial(n)))
    den='(s - ' + str(a) +')^' +str(n+1)
    return  num,den

def sinh(a,b) :
    num=str(int(a*b))
    den='s^2 - '+str(int(math.pow(b,2)))
    return num,den

def cosh(a,b) :
    num=str(a)+'s'
    den='(s^2 - '+str(int(math.pow(b,2)))+')'
    return num,den
