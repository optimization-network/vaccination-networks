# -*- coding: utf-8 -*-
"""
Toy model v 1.
"""
from gurobipy import *

""" Defines the Sets F, O   and J """
FixedHCs = ["F2",'F7']
Outreaches = ['O1','O3','O4','O5','O6','O8','O9']
Regions= ["Reg1",'Reg2', 'Reg3', 'Reg4','Reg5','Reg6','Reg7','Reg8', 'Reg9']

Emin =4 
Ce = 400
Ve = 100
Co = 5000
Vo = 1000
Budget=58000
    

"""Population region"""
Re = {'Reg1':535,'Reg2':2000, 'Reg3':535, 'Reg4':535,'Reg5':535,'Reg6':535,'Reg7':2500,'Reg8':535, 'Reg9':535}

"""demand"""
dfj = {
    "F2": {   "Reg1": 374.5, "Reg2": 1980, "Reg3": 428, "Reg4": 385.2, "Reg5": 363.8, "Reg6": 321, "Reg7": 450, "Reg8": 160.5, "Reg9": 0},
    "F7": {   "Reg1": 0, "Reg2": 360, "Reg3": 160.5, "Reg4": 171.2, "Reg5": 374.5, "Reg6": 363.8, "Reg7": 2475, "Reg8": 374.5, "Reg9": 428}
}
doj = {
    "O1": {   "Reg1": 529.65, "Reg2": 1400, "Reg3": 428, "Reg4": 53.5, "Reg5": 107, "Reg6": 160.5, "Reg7": 0, "Reg8": 0, "Reg9": 0},
    "O2": {   "Reg1": 374.5, "Reg2": 1980, "Reg3": 428, "Reg4": 385.2, "Reg5": 363.8, "Reg6": 321, "Reg7": 450, "Reg8": 160.5, "Reg9": 0},
    "O3": {   "Reg1": 428, "Reg2": 1600, "Reg3": 529.65, "Reg4": 321, "Reg5": 374.5, "Reg6": 428, "Reg7": 750, "Reg8": 160.5, "Reg9": 107},
    "O4": {   "Reg1": 53.5, "Reg2": 1440, "Reg3": 321, "Reg4": 529.65, "Reg5": 428, "Reg6": 321, "Reg7": 800, "Reg8": 374.5, "Reg9": 160.5},
    "O5": {   "Reg1": 107, "Reg2": 1360, "Reg3": 374.5, "Reg4": 428, "Reg5": 529.65, "Reg6": 428, "Reg7": 1750, "Reg8": 417.3, "Reg9": 267.5},
    "O6": {   "Reg1": 160.5, "Reg2": 1200, "Reg3": 428, "Reg4": 321, "Reg5": 428, "Reg6": 529.65, "Reg7": 1700, "Reg8": 321, "Reg9": 224.7},
    "O7": {   "Reg1": 0, "Reg2": 360, "Reg3": 160.5, "Reg4": 171.2, "Reg5": 374.5, "Reg6": 363.8, "Reg7": 2475, "Reg8": 374.5, "Reg9": 428},
    "O8": {   "Reg1": 0, "Reg2": 600, "Reg3": 160.5, "Reg4": 374.5, "Reg5": 417.3, "Reg6": 321, "Reg7": 1750, "Reg8": 529.65, "Reg9": 374.5},
    "O9": {   "Reg1": 0, "Reg2": 0, "Reg3": 107, "Reg4": 160.5, "Reg5": 267.5, "Reg6": 224.7, "Reg7": 2000, "Reg8": 374.5, "Reg9": 529.65}
    }
cfj = {   
    "F2": {   "Reg1": 8.5, "Reg2": 1.25, "Reg3": 6, "Reg4": 8, "Reg5": 9, "Reg6": 11, "Reg7": 21.5, "Reg8": 18.5, "Reg9": 31},
    "F7": {   "Reg1": 31, "Reg2": 21.5, "Reg3": 18.5, "Reg4": 18, "Reg5": 8.5, "Reg6": 9, "Reg7": 1.25, "Reg8": 8.5, "Reg9": 6}
      }  

coj = {          
    "O1": {   "Reg1": 1.25, "Reg2": 8.5, "Reg3": 6, "Reg4": 23.5, "Reg5": 21, "Reg6": 18.5, "Reg7": 31, "Reg8": 38.5, "Reg9": 41},
    "O3": {   "Reg1": 6, "Reg2": 6, "Reg3": 1.25, "Reg4": 11, "Reg5": 8.5, "Reg6": 6, "Reg7": 18.5, "Reg8": 18.5, "Reg9": 21},
    "O4": {   "Reg1": 23.5, "Reg2": 8, "Reg3": 11, "Reg4": 1.25, "Reg5": 6, "Reg6": 11, "Reg7": 18, "Reg8": 8.5, "Reg9": 18.5},
    "O5": {   "Reg1": 21, "Reg2": 9, "Reg3": 8.5, "Reg4": 6, "Reg5": 1.25, "Reg6": 6, "Reg7": 8.5, "Reg8": 6.5, "Reg9": 13.5},
    "O6": {   "Reg1": 18.5, "Reg2": 11, "Reg3": 6, "Reg4": 11, "Reg5": 6, "Reg6": 1.25, "Reg7": 9, "Reg8": 11, "Reg9": 15.5},
    "O8": {   "Reg1": 38.5, "Reg2": 18.5, "Reg3": 18.5, "Reg4": 8.5, "Reg5": 6.5, "Reg6": 11, "Reg7": 8.5, "Reg8": 1.25, "Reg9": 8.5},
    "O9": {   "Reg1": 41, "Reg2": 31, "Reg3": 21, "Reg4": 18.5, "Reg5": 13.5, "Reg6": 15.5, "Reg7": 6, "Reg8": 8.5, "Reg9": 1.25}
     }

model = Model ('Toy model V1')

Xfj=  model.addVars(FixedHCs, Regions, vtype=GRB.CONTINUOUS, name = 'Xfj')
Xoj = model.addVars(Outreaches, Regions,vtype=GRB.CONTINUOUS,  name = 'Xoj')
Ef = model.addVars(FixedHCs,vtype=GRB.CONTINUOUS, name = 'Ef')
Zo = model.addVars(Outreaches, vtype=GRB.BINARY, name = 'Zo')
Yfj=  model.addVars(FixedHCs, Regions, vtype=GRB.BINARY, name = 'Yfj')
Yoj = model.addVars(Outreaches, Regions, vtype=GRB.BINARY, name = 'Yoj')

model.update()

model.addConstrs( (Xfj[FixedHC,Region]  <= dfj[FixedHC][Region]*Yfj[FixedHC,Region] for FixedHC in FixedHCs for Region in Regions), name = '(1) Demandfc')        
model.addConstrs( (Xoj[Outreach,Region]  <= doj[Outreach][Region]*Yoj[Outreach,Region] for Outreach in Outreaches for Region in Regions), name = '(2) Demandor')


model.addConstrs( ( quicksum(Xfj[FixedHC,Region]for Region in Regions)  <= (Ef[FixedHC] * Ve) for FixedHC in FixedHCs ), name = "(4) Fixed HC Capacity")   
model.addConstrs( ( quicksum(Xoj[Outreach,Region]for Region in Regions)  <= Vo* Zo[Outreach] for Outreach in Outreaches ), name = "(5) Outreaches Capacity")   

model.addConstrs( (
        quicksum(Yfj[FixedHC,Region ]for FixedHC in FixedHCs)+ 
        quicksum(Yoj[Outreach,Region]for Outreach in Outreaches)
                                        <= 1 for Region in Regions), name = "(7) Single Alocation") 
model.addConstr( (
        quicksum(Ef[FixedHC] * Ce for FixedHC in FixedHCs) + 
        quicksum(Zo[Outreach] * Co for Outreach in Outreaches) +
        quicksum(cfj[FixedHC][Region]*Xfj[FixedHC,Region] for FixedHC  in FixedHCs for Region in Regions)+
        quicksum(coj[Outreach][Region] * Xoj[Outreach,Region] for Outreach in Outreaches for Region in Regions) <= Budget), name = "(6) Budget")    
    

obj = ( quicksum(Xfj[FixedHC,Region]  for FixedHC  in FixedHCs for Region in Regions)+
        quicksum(Xoj[Outreach,Region] for Outreach in Outreaches for Region in Regions))

model.setObjective(obj, GRB.MAXIMIZE)   
model.optimize()
model.printAttr('X')