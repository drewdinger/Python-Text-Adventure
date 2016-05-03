# Project Text Adventure WOW! Andrew Krodinger
# 4 funtions !!!!
# 2 loops !!
# 4 if/elif/else !!!
# 4 numerical values !!!!
# 4 strings !!!!
# 2 classes or file I/O !!

class Myclass:
	def __init__(self, number):
		self.x = number
a = Myclass(1)
b = Myclass(2)
c = Myclass(3)
d = Myclass(4)

class player:
	def __init__(self, playerName,):
		self.pname = playerName
		def winner(self):
			self.areyouawinner = True

def main():
	def bench():
		mystr7 = input("On the bench you see A Tale of Two Cities. Do you (R)ead the book or (T)ake a nap?")
		while mystr7 != "R" and mystr7 != "T":
			print("Not a valid option.")
			mystr7 = input("On the bench you see A Tale of Two Cities. Do you (R)ead the book or (T)ake a nap?")
		if mystr7 == "R":
			print("Congratulations! Intelligence +",c.x,"Strength -",b.x,".")
		else:
			print("Congratulations! Stamina Restored. All status ailments cured. All stats +",a.x)
	def pullup():
		mystr6 = input("You see the pullup bar. Do you do (P)ullups or (D)aydream about doing pullups?")
		while mystr6 != "P" and mystr6 != "D":
			print("Not a valid option.")
			mystr6 = input("You see the pullup bar. Do you do (P)ullups or (D)aydream about doing pullups?")
		if mystr6 == "P":
			print("Congratulations! Strength +",d.x,"Intelligence -",d.x,".")
		else:
			print("Congratulations! All stats -",d.x)
	def upstairs():
		mystr5 = input("You are in your room. You see your bed and your laptop. Do you want to (S)leep or check (R)eddit? ")
		while mystr5 != "S" and mystr5 != "R":
			print("Not a valid option.")
			mystr5 = input("You are in your room. You see your bed and your laptop. Do you want to (S)leep or check (R)eddit? ")
		if mystr5 == "S":
			print("Congratulations! Endurance +",d.x,"Intelligence -",a.x,".")
		else:
			print("Congratulations! All stats +",d.x)
	def couch():
		mystr4 = input("Sitting on the couch you see your Playstation and the T.V. remote. Do you play (S)treet Fighter 4 or do you (W)atch shark week? ")
		while mystr4 != "S" and mystr4 != "W":
			print("Not a valid option.")
			mystr4 = input("Sitting on the couch you see your Playstation and the T.V. remote. Do you play (S)treet Fighter 4 or do you (W)atch shark week? ")
		if mystr4 == "S":
			print("Congratulations! Dexterity +",b.x,"Strength -",a.x,".")
		else:
			print("Congratulations! Intelligence +",c.x,"Strength -",b.x,".")
	def side():
		mystr3 = input("On the side of the house you see a pullup bar and a bench with a book on it. Do you walk over to the (P)ullup bar or sit down on the (B)ench? ")
		while mystr3 != "P" and mystr3 != "B":
			print("Not a valid option.")
			mystr3 = input("On the side of the house you see a pullup bar and a bench with a book on it. Do you walk over to the (P)ullup bar or sit down on the (B)ench? ")
		if mystr3 == "P":
			print("You Walk over to the pullup bar.")
			pullup()
		else:
			print("You sat on the bench.")
			bench()
	def inside():
		mystr2 = input("Inside the house you see the couch in the living room and stairs to your bedroom. Do you (S)it on the couch or do you go (U)pstairs? ")
		while mystr2 != "S" and  mystr2 != "U":
			print("Not a valid option.")
			mystr2 = input("Inside the house you see the couch in the living room and stairs to your bedroom. Do you (S)it on the couch or do you go (U)pstairs? ")
		if mystr2 == "S":
			print("You sat on the couch.")
			couch()
		else:
			print("You went upstairs.")
			upstairs()
	name = input("Input your name: ")
	Player = player(name)
	print("Hello",Player.pname)
	print("Let's Begin")
	print("Welcome to Text Adventure WOW!")
	mystr = input("You find yourself outside of your house. Do you (G)o inside, or do you (W)alk around to the side of your house? ")
	while mystr != "G" and mystr != "W":
		print("Not a valid option.")
		mystr = input("You find yourself outside of your house. Do you (G)o inside, or do you (W)alk around to the side of your house?")
	if mystr == "G":
		print("You went inside.")
		inside()
	else:
		print("You went to the side of the house.")
		side()
		
main()











