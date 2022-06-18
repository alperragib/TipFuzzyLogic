import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control

kalite = control.Antecedent(np.arange(0,11,1),"kalite")
servis = control.Antecedent(np.arange(0,11,1),"servis")
bahsis = control.Consequent(np.arange(0,26,1),"bahşiş")

kalite.automf(3)
servis.automf(3)

bahsis["düşük"] = fuzzy.trimf(bahsis.universe, [0,0,13])
bahsis["orta"] = fuzzy.trimf(bahsis.universe, [0,13,25])
bahsis["yüksek"] = fuzzy.trimf(bahsis.universe, [13,25,25])

kural1 = control.Rule(kalite["good"] | servis["good"], bahsis["yüksek"])
kural2 = control.Rule(servis["average"], bahsis["orta"])
kural3 = control.Rule(kalite["poor"] | servis["poor"], bahsis["düşük"])

bahsis_kontrol = control.ControlSystem([kural1, kural2, kural3])
bahsis_belirleme = control.ControlSystemSimulation(bahsis_kontrol)

bahsis_belirleme.input["kalite"] = 3.2
bahsis_belirleme.input["servis"] = 2.4
bahsis_belirleme.compute()

print(bahsis_belirleme.output["bahşiş"])

bahsis.view(sim=bahsis_belirleme)