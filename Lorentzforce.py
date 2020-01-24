# Lorentz Force Trajectory Calculator
# defining constant values as 1
q = -1 #charge of the particle
dt = 0.01
m = 1 #mass of the particle

file = open("LorentzForceTrajectory.txt", "w")

Ex, Ey, Ez = (input(
    "Enter the X,Y,Z components of the Electric field respectively in V/m: ")).split(",")
Bx, By, Bz = (
    input("Enter the X,Y,Z components of the Magnetic field in Tesla: ")).split(",")
E0 = [Ex, Ey, Ez]
B0 = [Bx, By, Bz]

E = []
B = []
for i in range(3):
    E.append(float(E0[i]))  # turning data to the float
    B.append(float(B0[i]))


Vi = [0, 0, 0]   # initial velocity
Ri = [0, 0, 0]  # inital position


def acc(V, B):
    Ax = (q/m)*(E[0]+(V[1]*B[2]-V[2]*B[1]))
    Ay = (q/m)*(E[1]+(V[2]*B[0]-V[0]*B[2]))
    Az = (q/m)*(E[2]+(V[0]*B[1]-V[1]*B[0]))
    A = [Ax, Ay, Az]
    return A


k = acc(Vi, B)  # calculating the inital acceleration
for n in range(1200):
    # defining the x component of the position
    Xn = Ri[0]+dt*Vi[0]+1/2*dt*dt*k[0]
    # defining the y component of the position
    Yn = Ri[1]+dt*Vi[1]+1/2*dt*dt*k[1]
    # defining the z component of the position
    Zn = Ri[2]+dt*Vi[2]+1/2*dt*dt*k[2]
    # printing these components into the file
    file.write("%.5f %4.5f %4.5f\n" % (Xn, Yn, Zn))
    Rn = [Xn, Yn, Zn]  # taking these values to an array
    W = []  # defining an array that will calculate the acceleration for the next steps
    for i in range(3):
        N = Vi[i]+dt*k[i]
        W.append(N)
    l = acc(W, B)
    Vtx = Vi[0]+1/2*dt*(k[0]+l[0])
    Vty = Vi[1]+1/2*dt*(k[1]+l[1])
    Vtz = Vi[2]+1/2*dt*(k[2]+l[2])
    Vtemp = [Vtx, Vty, Vtz]  # temporary velocity
    C = acc(Vtemp, B)
    Vnx = Vi[0]+1/2*dt*(k[0]+C[0])
    Vny = Vi[1]+1/2*dt*(k[1]+C[1])
    Vnz = Vi[2]+1/2*dt*(k[2]+C[2])
    Vnext = [Vnx, Vny, Vnz]  # the next velocity
    # defining the cross product corresponding to the next velocity
    k = acc(Vnext, B)
    Vi = Vnext
    Ri = Rn
    W = []
file.close()
