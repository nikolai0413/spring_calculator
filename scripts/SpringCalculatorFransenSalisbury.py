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



endType = 'plain'
material  = 'A229'
wireDiameter = 0.004 #in

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

propRow  = 1

if material == 'A313':
    print(material)
    #Special stuff choose row
elif material == 'B159':
    #Properties = row of prop table
    print(material)
    #Special stuff choose row
else:
    print(material)
    pitch = 0
    #Easy choose row 


#thisWireProperties = propTable10_4[][]

#ultimateTensileStrength = A/d**m

