class PlayerItens:
	def showDetails(self):
		return self.__class__.__name__
	
	def returnTotalPrice(self):
		return self.__class__.price
		
class Player(PlayerItens):
	price = 0
	
class Decorator(PlayerItens):
	def __init__(self, playerItens):
		self.itens = playerItens
		
	def returnTotalPrice(self):
		return self.itens.returnTotalPrice() + PlayerItens.returnTotalPrice(self)
		
	def showDetails(self):
		return self.itens.showDetails() + ' ' + PlayerItens.showDetails(self)

#-------------------------Meelee Weapons-------------------------#

class Knife(Decorator):
	price = 0
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

		
		
#-------------------------Ranged Weapons-------------------------#

#Pistols
class Glock(Decorator):
	price = 400
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)
		
class USP(Decorator):
	price = 500
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)
		
class P228(Decorator):
	price = 600
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class DesertEagle(Decorator):
	price = 650
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class FiveSevenN(Decorator):
	price = 750
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class DualBerettas(Decorator):
	price = 800
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

				
#Shotguns
class M3(Decorator):
	price = 1700
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class LeoneYG(Decorator):
	price = 3000
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

#Submachine guns
class TMP(Decorator):
	price = 1250
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)
		return self.type, self.subtype	

class MAC10(Decorator):
	price = 1400
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class MP5(Decorator):
	price = 1500
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)
		
class UMP45(Decorator):
	price = 1700
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)
		
class P90(Decorator):
	price = 2350
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

#Machine guns
class M249(Decorator):
	price = 5750
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

#Rifles
class IMI(Decorator):
	price = 2000
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)
		
class FAMAS(Decorator):
	price = 2250
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class AKA47(Decorator):
	price = 2500
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class M4(Decorator):
	price = 3100
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)	

class Scout(Decorator):
	price = 2750
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class SG552(Decorator):
	price = 3500
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class Bullpup(Decorator):
	price = 3500
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class D3AU1(Decorator):
	price = 5000
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)	

class Krieg550(Decorator):
	price = 4200
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class AWP(Decorator):
	price = 4750
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)


#-------------------------Equipments-------------------------#	

#Grenades
class HE(Decorator):
	price = 300
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)

class Flashbang(Decorator):
	price = 200
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)	

class Smoke(Decorator):
	price = 300
	def __init__(self, playerItens):
		Decorator.__init__(self, playerItens)


terrorist = AKA47(HE(Player()))

print(terrorist.showDetails().strip() + "price: US$", (terrorist.returnTotalPrice()))