from Robot2I013 import Robot2I013
import math
import time
from PIL.Image import *


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
		print("rotation")
		if sens > 0 :
				self.set_speed(-50 , 50)
		else :
				self.set_speed(50 , -50)

	def update(self):
		""" Exemple de fonction update : 																																																																																																																																																																																																																																																																																																																																																																									
			Pour 50 pas fait avancer le robot, puis le tourne pour 20 pas puis s'arrete.
			Affiche la distance et enregistre une image tous les 10 pas, tourne la tete a gauche et a droite. 
		"""


		""" couleur rouge : R > 200 , V < 100 et B < 100
					vert : V > 200 , R <100 et B < 100
					bleu : B > 200, R < 100 , V < 100
					Jaune :
					"""

		img = self.robot.get_image()
		img.save("images/balise.jpeg" , "JPEG")
		img = open("images/balise.jpeg")
		(l , h) = img.size
		cptr,cptj,cptb,cptv = 0,0,0,0
		for i in range(h//2 - h/10 , h/2 + h/10) : 
			for j in range(l/2 -l/10 , l/2 + l/10) :
				pix = Image.getpixel(img , (j , i))
				if pix[0] > 150 and pix[1] < 90 and pix[2] < 90 : #Rouge
					cptr += 1
				elif pix[1] > 150 and pix[0] < 90 and pix[2] < 90 : #Vert
					cptb += 1

				elif pix[2] > 150 and pix[1] < 90 and pix[0] < 90 :	#Blue	
					cptv += 1
				elif pix[0] > 150 and pix[1] > 90 and pix[2] < 90 : #jaune
					cptj +=1

		print(cptr, cptb,cptv , cptj)
		

		if cptr + cptj + cptb + cptv > 8000 :
			self.stop = True
		if cptr + cptj + cptb + cptv > 4000 :
			if cptb + cptv > cptj + cptb:
				self.robot.set_motor_dps(1 , 50)
				self.robot.set_motor_dps(2 , 25)
			else :
				self.robot.set_motor_dps(2,50)
				self.robot.set_motor_dps(1,25)
		
			
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
