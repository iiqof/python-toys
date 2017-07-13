from sympy import symbols, Matrix, exp, I, sinh, cosh

z, w = symbols('z w')


#Lift: C-->C^2; z-->(z,1)^T

def Lift(z):
    return Matrix([[z],[1]])

#Proj:C^2-->C; (z,w)^T-->z/w


def Proj(z):
    return z[0]/z[1]



#Action of SU(1,1) in D

def Action(M,z):
    return Proj(M*Lift(z))

# Some actions

def R(theta): # Rotation
    return Matrix([[exp(I*theta/2),0],[0,exp(-I*theta/2)]])

def Tx(x):
    return Matrix([[cosh(x/2),sinh(x/2)],[sinh(x/2), cosh(x/2)]])
