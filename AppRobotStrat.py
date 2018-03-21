from gl_lib.sim.affichage.d2.interface.AppRobot import AppRobot
from gl_lib.sim.robot import *
from gl_lib.sim.geometrie.point import *
from gl_lib.sim.geometrie import Arene
from time import sleep
from tkinter import *
from gl_lib.sim.robot.strategie.DeplacementCarre import *


class AppRobotStrat(AppRobot):
    PAS_TEMPS = 0.015

    def __init__(self, robot: RobotAutonome, arene: Arene, strat):

        AppRobot.__init__(self, robot, arene)
        self.strat=strat

    def keyCommand(self, event):
        """
        dirige le robot selon la touche tapee
        """
        self.canvas.delete(ALL)
        self.update()
        touche = event.keysym
        if touche == 'z':
            self.strat.run()

        self.update()

    def updateValues(self):
        """
        Met a jour les vitesses, et la position du robot
        """
        self.robot.vitesse = float(self.vitesse.get())
        self.robot.vitesseRot = float(self.strat.angle)

    def updateCanvas(self):
        """
        Met a jour le canvas
        """
        self.canvas.delete(ALL)
        self.arene.afficher(self.canvas)
        self.canvas.update()

    def update(self):
        """
        Met a jour les vitesses, la simulation du mouvement du robot et l'affichage
        """
        self.updateValues()
        self.updateCanvas()