from Robot2I013 import Robot2I013
import math
import time


class Controller(object):
	def __init__(self):
		""" Initialise le controleur et un robot """
		self.robot = Robot2I013(self,fps=10.)
		self.cpt = 0
		self.cpt_rot = 0
		self.rot_bool = False
		self.anglePrec = self.robot.get_motor_position()[0]
		
	def set_led(self,col):
		""" Allume les leds du robot au triplet col=(r,g,b) """
		self.robot.set_led(self.robot.LED_LEFT_EYE+self.robot.LED_RIGHT_EYE,*col)

	def set_speed(self,lspeed,rspeed):
		""" Fait tourner les moteurs a la vitesse lspeed pour le moteur gauche, rspeed pour le moteur droit """
		self.robot.set_motor_dps(self.robot.MOTOR_LEFT,lspeed)
		self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,rspeed)

	def forward(self,speed):
		""" Avant le robot a la vitesse speed """
		self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,speed)

	def rotate(self , sens) :
		if sens > 0 :
				self.set_speed(0 , 50)
		else :
				self.set_speed(50 , 0)

	def update(self):
		""" Exemple de fonction update : 
			Pour 50 pas fait avancer le robot, puis le tourne pour 20 pas puis s'arrete.
			Affiche la distance et enregistre une image tous les 10 pas, tourne la tete a gauche et a droite. 
		"""

		if not self.rot_bool :
			self.cpt += self.distparcourue()
			if self.cpt > 700 :
				if self.cpt_rot < 4 :
					self.rot_bool = True
					self.anglePrec = self.robot.get_motor_position()
				else : 
					self.robot.stop()
					self.stop = True
			elif self.cpt > 500. :
				self.forward(100)
			else :
				self.forward(200)
		else :
			if ((self.robot.get_motor_position()[0] - self.anglePrec[0])*math.pi*self.robot.WHEEL_DIAMETER / 360 ) * self.robot.WHEEL_BASE_WIDTH < math.pi / 2 : 
				self.rotate(1)
			else :
				self.rot_bool = False
				self.cpt_rot += 1
				self.cpt = 0
			
		return
		
	def run(self):
		self.stop=False
		self.robot.run()

	def distparcourue(self):
		var =  (self.robot.get_motor_position()[0] - self.anglePrec )*math.pi*self.robot.WHEEL_DIAMETER / 360
		self.anglePrec = self.robot.get_motor_position()[0]
		return var
if __name__=="__main__":
	ctrl = Controller()
	ctrl.run()
