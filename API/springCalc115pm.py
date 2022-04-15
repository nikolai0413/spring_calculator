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
# Free length (L0)
# Solid length (Ls)

#OUTPUTS
# The pitch, p
# The number of total coils (Nt) and the number of active coils (Na)
# The spring rate, k
# The force needed to compress the spring to its solid length and the factor of safety for static yielding
# when the spring is compressed to this length
# For a static load, the Spring Calculator should find the factor of safety.
# For a cyclic load (i.e., Fmax and Fmin), the Spring Calculator should find the factor of safety for infinite life.



material  = 'A228'
d = 0.1 #in
D = 1.0 

# ---------------- End Type ---------------- 
endType = 'plain'

nEnd = 0
nTotal = 0
nActive = 0

Ls = 5.0
L0 = 8.0
pitch = 0

if endType == 'plain':
    print(endType)
    nEnd = 0
    nTotal = Ls/d-1
    nActive = nTotal - nEnd
    pitch = (L0-d)/nActive

elif endType == 'plainAndGround':
    print(endType)
    nEnd = 1
    nTotal = Ls/d
    nActive = nTotal - nEnd
    pitch = (L0)/(nActive+1)

elif endType == 'squaredOrClosed':
    print(endType)
    nEnd = 2
    nTotal = Ls/d-1
    nActive = nTotal - nEnd
    pitch = (L0-3*d)/nActive
    
elif endType == 'squaredAndGround':
    print(endType)    
    nEnd = 2  
    nTotal = Ls/d
    nActive = nTotal - nEnd
    pitch = (L0-2*d)/nActive
    

print(nEnd, nTotal, nActive, pitch)





if(d < 0.004):
    print('Too small a wire')

#Shigley 10-4: "ASTM Code", exponent m, d_min [in], d_max [in], A kpsi-in
propTable10_4 = np.array([["A228", 0.145, 0.004, 0.256, 201],
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

prop4Row  = 1
improperSize = False

if material == 'A313':
    print(material)
    prop4Row = 5
    if d < float(propTable10_4[prop4Row,2]):
        improperSize = True
        print("bad size")
    elif d < float(propTable10_4[prop4Row,3]):
        print('prop4Row = ', prop4Row)
        #this is fine
    elif d < float(propTable10_4[prop4Row+1,3]):
        prop4Row +=1 
    elif d < float(propTable10_4[prop4Row+2,3]):
        prop4Row +=2 
    else:
        improperSize = True
        print("bad size")
    
elif material == 'B159':
    print(material)
    prop4Row = 8
    if d < float(propTable10_4[prop4Row,2]):
        improperSize = True
        print("bad size")
    elif d < float(propTable10_4[prop4Row,3]):
        print('prop4Row = ', prop4Row)
        #this is fine
    elif d < float(propTable10_4[prop4Row+1,3]):
        prop4Row +=1 
    elif d < float(propTable10_4[prop4Row+2,3]):
        prop4Row +=2
    else:
        improperSize = True
        print("bad size")

elif material == 'A228':
    prop4Row = 0
elif material == 'A229':
    prop4Row = 1
elif material == 'A227':
    prop4Row = 2
elif material == 'A232':
    prop4Row = 3
elif material == 'A401':
    prop4Row = 4
else:
    print('invalid material')

print(float(propTable10_4[prop4Row,2]))
print('test')

if d < float(propTable10_4[prop4Row,2]) or d > float(propTable10_4[prop4Row,3]):
    improperSize = True
    print("bad size")

properties4 = propTable10_4[prop4Row,:]

ultimateTensileStrength = float(properties4[4]) * d **(-1*float(properties4[1])) #A/d**m



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
    if d < float(propTable10_5[prop5Row,4]):
        print("good")
    elif d < float(propTable10_5[prop5Row+1,4]):
        prop5Row +=1 
        print('prop5Row = ', prop5Row)
    elif d < float(propTable10_5[prop5Row+2,4]):
        prop5Row +=2 
        print('prop5Row = ', prop5Row)
    elif d < float(propTable10_5[prop5Row+3,4]):
        prop5Row +=3
        print('prop5Row = ', prop5Row)
    else:
        improperSize = True
        print("bad size")
    
elif material == 'A227':
    print(material)
    prop5Row = 4
    if d < float(propTable10_5[prop5Row,4]):
        print("good")
    elif d < float(propTable10_5[prop5Row+1,4]):
        prop5Row +=1 
        print('prop5Row = ', prop5Row)
    elif d < float(propTable10_5[prop5Row+2,4]):
        prop5Row +=2 
        print('prop5Row = ', prop5Row)
    elif d < float(propTable10_5[prop5Row+3,4]):
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



properties5 = propTable10_5[prop5Row,:]

G = properties5[6]


if material == 'A228' or material == 'A227':
    sSY = 0.45*ultimateTensileStrength
elif material == '0':
    sSY = 0.5*ultimateTensileStrength
elif material == 'A313':
    sSY = 0.35*ultimateTensileStrength
elif material == 'A401' or material == 'A232' or material == 'B159':
    sSY = 0.35*ultimateTensileStrength     

# Calculation of spring rate
C = D/d
kB = (4*C+2)/(4*C-3)
k = d**4 * float(G) / (8 * D)

# STATIC ANALYSIS
# SOLID LENGTH
fShut = k * (L0-Ls) # __________ OUTPUT __________
tauS = kB * 8 * fShut * D / (np.pi * d**3)
nShut = sSY / tauS # __________ OUTPUT __________

fInput = 50.0 # __________ INPUT __________
tauFInput = kB * 8 * fInput * D / (np.pi * d**3)
nStatic = sSY / tauFInput # __________ OUTPUT __________



# FATIGUE ANALYSIS
fMax = 50.0 # __________ INPUT __________
fMin = 20.0# __________ INPUT __________

fA = (fMax - fMin)/2
fM = (fMax + fMin)/2

tA = kB * 8 * fA * D / (np.pi * d**3)
tM = kB * 8 * fM * D / (np.pi * d**3)

sSA_psi = 35,000 # Unpeened
sSM_psi = 55,000 # Unpeened
sSU = 0.67 * ultimateTensileStrength# Unpeened

sSE = sSA_psi/ (1 - sSM_psi /sSU)

nFatigue = (tA/sSE + tM/sSU)**(-1) # __________ OUTPUT __________

# TESTING
print('prop4Row = ', prop4Row)
print(propTable10_4[prop4Row,:])

print('prop5Row = ', prop5Row)
print(propTable10_5[prop5Row,:])

