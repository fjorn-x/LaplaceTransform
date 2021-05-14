import math

def constant(a,b) :
   return str(a) +'s';

def expo(constant,b) :
    return str(1) +' / ' + '(s - ' + str(constant) + ')'

def tfunc(constant,b) :
    fact=int(math.factorial(constant))
    return str(fact) + ' / ' + '(s^'+str(constant+1)+')'

def sine(a,b) :
    return str(a*b) + " / " +"(s^2 + " + str(int(math.pow(b,2))) +" )"

def cos(a,b) :
    return  str(a*b)+"s / " +"(s^2 + " + str(int(math.pow(b,2))) +" )"

def expo_sin(a, b): 
    return str(b) + ' / ' + '((s - ' + str(a) + ')^2 + '+str(int(math.pow(b,2))) + ')'

def expo_cos(a, b): 
    return '(s - '+str(a)+')'+ '/' + '((s - ' + str(a) + ')^2 + '+str(int(math.pow(b,2))) + ')'

def expo_sinh(a, b): 
    return str(b) + ' / ' + '((s - ' + str(a) + ')^2 - '+str(int(math.pow(b,2))) + ')'

def expo_cosh(a, b): 
    return '(s - '+str(a)+')'+ '/' + '((s - ' + str(a) + ')^2 - '+str(int(math.pow(b,2))) + ')'

def t_expo(n,a) :
    return str(int(math.factorial(n))) + ' / ' + '(s - ' + str(a) +')^' +str(n+1)

