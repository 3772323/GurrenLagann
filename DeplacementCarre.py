from gl_lib.sim.robot.strategie.Strategie import *
from gl_lib.sim.robot import *
from time import sleep
from gl_lib.sim.affichage.d2.interface.AppRobotStrat import *
from math import pi


class DeplacementCaree(Strategie):
    def __init__(self, robot):
        Strategie.__init__(self, robot)
        self.angle=pi/2
        self.cote=30

    def run(self):
        i=1
        self.robot.vitesseRot=pi/2
        while(i<=self.cote*4):
            if(i%self.cote==0):
                self.robot.tourner(-1)
                self.ctr.update()
                sleep(0.2)

            self.robot.avancer(1)
            self.ctr.update()
            sleep(0.2)
            i=i+1
            print(self.robot.centre)






