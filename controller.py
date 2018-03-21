from gl_lib.sim.affichage.d2.interface.AppRobotStrat import *
from gl_lib.sim.robot.strategie import *

class controller:
    def __init__(self, app):
        self.app=app

    def update(self):
        self.app.update()