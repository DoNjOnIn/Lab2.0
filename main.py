import math as m
x = float(input('x='))
r = float(input('R='))
if x<=-r:
    print("y="+str(r))
if x>-r and x<r:
    print('y='+str(r-m.sqrt(r*r-x*x)))
if x>=r and x<=6:
    print('y='+ str(r+((-3-r)/(6-r)*(x-r))))
if x>6:
    print('y='+str(x+9))
print('Hello world')
print('123')