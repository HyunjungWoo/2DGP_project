from vector import vector

import random

class Mover:
	def __init__(self,x = 0.0,y = 0.0 , mass = 1.0):
		self.location = vector(x,y)
		self.velocity = vector()
		slef.acceleration = vector()
		
		#질량
		self.mass = mass
		self.G = 1.0

		

	def applyForce(self,force):
	#뉴턴 운동 2법칙 (F= MA,A = F/M)
	force  /= vector(self.mass, self,mass)
	self.acceleration += force
