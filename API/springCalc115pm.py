import numpy as np

#inputs
#Materials
#choose a material
# pull values of ultimate strength, yield strength, elastic moduli (E and G) 

#INPUTS
# End type: (Plain), (Plain and ground), (Squared or closed), (Squared and ground)
# Material
# Wire diameter
# Outer diameter
# Free length (L0_in)
# Solid length (Ls_in)

#OUTPUTS
# The pitch_in_rev, p
# The number of total coils (Nt) and the number of active coils (Na)
# The spring rate, k
# The force needed to compress the spring to its solid length and the factor of safety for static yielding
# when the spring is compressed to this length
# For a static load, the Spring Calculator should find the factor of safety.
# For a cyclic load (i.e., Fmax and Fmin), the Spring Calculator should find the factor of safety for infinite life.


# ************** INPUTS ****************
material  = 'A313'
endType = 'squaredAndGround'
wireDiameter_in =  0.1
OD_in = 9/16
L0_in = 4 + 3/8
Ls_in = wireDiameter_in * 23; # for example 10-4


Fstatic_lbf = 30

F_max_lbf = 35
F_min_lbf = 5

# ******************************


# ************** OUTPUTS ****************
pitch_in_rev = None
nt_ = None
na_ = None
k_lbf_in = None
fShut_lbf = None
nShut_ = None

nStatic_ = None

nFatigue_ = None

# ******************************

nEnd_ = None


# perform outer to mean adjustment
meanDiam_in = OD_in - wireDiameter_in;

if endType == 'plain':
    print(endType)
    nEnd_ = 0
    nt_ = Ls_in/wireDiameter_in-1
    na_ = nt_ - nEnd_
    pitch_in_rev = (L0_in-wireDiameter_in)/na_

elif endType == 'plainAndGround':
    print(endType)
    nEnd_ = 1
    nt_ = Ls_in/wireDiameter_in
    na_ = nt_ - nEnd_
    pitch_in_rev = (L0_in)/(na_+1)

elif endType == 'squaredOrClosed':
    print(endType)
    nEnd_ = 2
    nt_ = Ls_in/wireDiameter_in-1
    na_ = nt_ - nEnd_
    pitch_in_rev = (L0_in-3*wireDiameter_in)/na_
    
elif endType == 'squaredAndGround':
    print(endType)    
    nEnd_ = 2  
    nt_ = Ls_in/wireDiameter_in
    na_ = nt_ - nEnd_
    pitch_in_rev = (L0_in-2*wireDiameter_in)/na_
else:
	print("weve got problems")
    

print(nEnd_, nt_, na_, pitch_in_rev)





if(wireDiameter_in < 0.004):
    	print("weve got problems")

#Shigley 10-4: "ASTM Code", exponent m, d_min [in], d_max [in], A kpsi-in
propTable10_4 = np.array([
["A228", 0.145, 0.004, 0.256, 201],
["A229", 0.187, 0.02, 0.5, 147],
["A227", 0.19, 0.028, 0.5, 140],
["A232", 0.168, 0.032, 0.437, 169],
["A401", 0.108, 0.063, 0.375, 202],
["A313", 0.146, 0.013, 0.1, 169],
["A313", 0.263, 0.1, 0.2, 128],
["A313", 0.478, 0.2, 0.4, 90],
["B159", 0, 0.004, 0.022, 145],
["B159", 0.028, 0.022, 0.075, 121],
["B159", 0.064, 0.075, 0.3, 110]])

table10_4_rowsel  = 1
improperSize = False

if material == 'A313':
    print(material)
    table10_4_rowsel = 5
    if wireDiameter_in < float(propTable10_4[table10_4_rowsel,2]):
        improperSize = True
        print("bad size")
    elif wireDiameter_in < float(propTable10_4[table10_4_rowsel,3]):
        print('table10_4_rowsel = ', table10_4_rowsel)
        #this is fine
    elif wireDiameter_in < float(propTable10_4[table10_4_rowsel+1,3]):
        table10_4_rowsel +=1 
    elif wireDiameter_in < float(propTable10_4[table10_4_rowsel+2,3]):
        table10_4_rowsel +=2 
    else:
        improperSize = True
        print("bad size")
    
elif material == 'B159':
    print(material)
    table10_4_rowsel = 8
    if wireDiameter_in < float(propTable10_4[table10_4_rowsel,2]):
        improperSize = True
        print("bad size")
    elif wireDiameter_in < float(propTable10_4[table10_4_rowsel,3]):
        print('table10_4_rowsel = ', table10_4_rowsel)
        #this is fine
    elif wireDiameter_in < float(propTable10_4[table10_4_rowsel+1,3]):
        table10_4_rowsel +=1 
    elif wireDiameter_in < float(propTable10_4[table10_4_rowsel+2,3]):
        table10_4_rowsel +=2
    else:
        improperSize = True
        print("bad size")

elif material == 'A228':
    table10_4_rowsel = 0
elif material == 'A229':
    table10_4_rowsel = 1
elif material == 'A227':
    table10_4_rowsel = 2
elif material == 'A232':
    table10_4_rowsel = 3
elif material == 'A401':
    table10_4_rowsel = 4
else:
    print('invalid material')


# print for debugging
print(float(propTable10_4[table10_4_rowsel,2]))
print('test')

# error handling
if wireDiameter_in < float(propTable10_4[table10_4_rowsel,2]) or wireDiameter_in > float(propTable10_4[table10_4_rowsel,3]):
    improperSize = True
    print("bad size")


# grabs the row
properties4 = propTable10_4[table10_4_rowsel,:]

A = float(properties4[4])
# UTS actually established
uts_kpsi = A * wireDiameter_in **(-1*float(properties4[1])) #A/d**m
uts_psi = uts_kpsi * 1000;




# ADD MORE PROPERTIES
#Shigley 10-5: "ASTM Code", % tensile, % torsion, d_min [in], d_max [in], E [Mpsi], G [Mpsi] 
propTable10_5 = np.array([["A228", 0.65, 0.45, 0, 0.032, 29.5, 12],
["A228", 0.65, 0.45, 0.032, 0.063, 29, 11.85],
["A228", 0.65, 0.45, 0.063, 0.125, 28.5, 11.75],
["A228", 0.65, 0.45, 0.125, 1, 28, 11.6],
["A227", 0.6, 0.45, 0, 0.032, 28.8, 11.7],
["A227", 0.6, 0.45, 0.032, 0.063, 28.7, 11.6],
["A227", 0.6, 0.45, 0.063, 0.125, 28.6, 11.5],
["A227", 0.6, 0.45, 0.125, 1, 28.5, 11.4],
["A232", 0.88, 0.65, 0, 1, 29.5, 11.2],
["A401", 0.85, 0.45, 0, 1, 29.5, 11.2],
["A313", 0.65, 0.8, 0, 1, 28, 10],
["B159", 0.75, 0.45, 0, 1, 15, 6]])


prop5Row  = 0

if material == 'A228':
    print(material)
    prop5Row = 0
    if wireDiameter_in < float(propTable10_5[prop5Row,4]):
        print("good")
    elif wireDiameter_in < float(propTable10_5[prop5Row+1,4]):
        prop5Row +=1 
        print('prop5Row = ', prop5Row)
    elif wireDiameter_in < float(propTable10_5[prop5Row+2,4]):
        prop5Row +=2 
        print('prop5Row = ', prop5Row)
    elif wireDiameter_in < float(propTable10_5[prop5Row+3,4]):
        prop5Row +=3
        print('prop5Row = ', prop5Row)
    else:
        improperSize = True
        print("bad size")
    
elif material == 'A227':
    print(material)
    prop5Row = 4
    if wireDiameter_in < float(propTable10_5[prop5Row,4]):
        print("good")
    elif wireDiameter_in < float(propTable10_5[prop5Row+1,4]):
        prop5Row +=1 
        print('prop5Row = ', prop5Row)
    elif wireDiameter_in < float(propTable10_5[prop5Row+2,4]):
        prop5Row +=2 
        print('prop5Row = ', prop5Row)
    elif wireDiameter_in < float(propTable10_5[prop5Row+3,4]):
        prop5Row +=3
        print('prop5Row = ', prop5Row)
    else:
        improperSize = True
        print("bad size")

elif material == 'A232':
    prop5Row = 8
elif material == 'A401':
    prop5Row = 9
elif material == 'A313':
    prop5Row = 10
elif material == 'B159':
    prop5Row = 11
elif material == 'A401':
    prop5Row = 12
else:
    print('invalid material')


# extract the row
properties5 = propTable10_5[prop5Row,:]

# get property
G_Mlbf_in2 = float(properties5[6])


if material == 'A228' or material == 'A227':
    sSY_psi = 0.45*uts_psi
elif material == '0':
    sSY_psi = 0.5*uts_psi
elif material == 'A313':
    sSY_psi = 0.35*uts_psi
elif material == 'A401' or material == 'A232' or material == 'B159':
    sSY_psi = 0.35*uts_psi     

# Calculation of spring rate
C_ = meanDiam_in/wireDiameter_in
kB_ = (4*C_+2)/(4*C_-3)
k_lbf_in = wireDiameter_in**4 * (G_Mlbf_in2 * 1e6) / (8 * meanDiam_in**3 * na_)

# STATIC ANALYSIS
# SOLID LENGTH
fShut_lbf = k_lbf_in * (L0_in-Ls_in) # __________ OUTPUT __________
tauS_lbf_in2 = kB_ * 8 * fShut_lbf * meanDiam_in / (np.pi * wireDiameter_in**3)
nShut_ = sSY_psi / tauS_lbf_in2 # __________ OUTPUT __________




tauFInput_psi = kB_ * 8 * Fstatic_lbf * meanDiam_in / (np.pi * wireDiameter_in**3)
nStatic_ = sSY_psi / tauFInput_psi # __________ OUTPUT __________


# *** FAtigue analysis

fA_lbf = (F_max_lbf - F_min_lbf)/2
fM_lbf = (F_max_lbf + F_min_lbf)/2

tA_psi = kB_ * 8 * fA_lbf * meanDiam_in / (np.pi * wireDiameter_in**3)
tM_psi = kB_ * 8 * fM_lbf * meanDiam_in / (np.pi * wireDiameter_in**3)

sSA_psi = 35000 # Unpeened
sSM_psi = 55000 # Unpeened
sSU_psi = 0.67 * uts_psi# Unpeened

sSE_psi = sSA_psi / (1 - sSM_psi / sSU_psi)

nFatigue_ = (tA_psi/sSE_psi + tM_psi/sSU_psi)**(-1) # __________ OUTPUT __________


print("done")