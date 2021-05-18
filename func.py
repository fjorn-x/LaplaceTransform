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
    return str(fact*constant) + ' / ' + '(s^'+str(b+1)+')'

def sine(a,b) :
    return str(a*b) + " / " +"(s^2 + " + str(int(math.pow(b,2))) +" )"

def cos(a,b) :
    return  str(a*b)+"s / " +"(s^2 + " + str(int(math.pow(b,2))) +" )"

def expo_sin(a, b): 
    return str(b) + ' / ' + '((s - ' + str(a) + ')^2 + '+str(int(math.pow(b,2))) + ')'

def expo_cos(a, b): 
    return '(s - ('+str(a)+'))'+ '/' + '((s - ' + str(a) + ')^2 + '+str(int(math.pow(b,2))) + ')'

def expo_sinh(a, b): 
    return str(b) + ' / ' + '((s - ' + str(a) + ')^2 - '+str(int(math.pow(b,2))) + ')'

def expo_cosh(a, b): 
    return '(s - '+str(a)+')'+ '/' + '((s - ' + str(a) + ')^2 - '+str(int(math.pow(b,2))) + ')'

def t_expo(n,a) :
    return str(int(math.factorial(n))) + ' / ' + '(s - ' + str(a) +')^' +str(n+1)

def sinh(a,b) :
    return str(int(a*b) )+' / (s^2 - '+str(int(math.pow(b,2)))+')'

def cosh(a,b) :
    return str(a)+'s / (s^2 - '+str(int(math.pow(b,2)))+')'
