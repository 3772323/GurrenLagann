from gl_lib.sim.affichage.d2 import *
from gl_lib.sim.robot import *
from gl_lib.sim.geometrie import *
from gl_lib.sim.robot.strategie.DeplacementCarre import *
from gl_lib.sim.affichage.d2.interface.AppRobotStrat import *
from gl_lib.sim.robot.strategie.controller import *

r=RobotPhysique(Pave(50,50,0), Objet3D(), Objet3D(), point.Vecteur(0, -1, 0))
a=Arene(400, [r] ,400)
v=r.direction.clone()
r.tete.addsensor(capteur.CapteurIR(r.tete))
r.deplacer(point.Vecteur(100, 300, 0))
strat=DeplacementCaree(r)
app=AppRobotStrat(r, vue.Vue2DArene(a), strat)
ctr=controller(app)
strat.ctr=ctr
app.init()

app.mainloop()
