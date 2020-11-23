# Introduction to Class
# class Team:
#     def __init__(self, Name="Name", Origin="Origin"):
#         self.TeamName = Name
#         self.TeamOrigin = Origin
#     def defineTeamName(self,TeamName):
#         self.TeamName = TeamName
#     def defineTeamOrigin(self,TeamOrigin):
#         self.TeamOrigin = TeamOrigin

# Team1 = Team("Tigers","Chicago")
# Team2 = Team("Hawks","South Africa")
# Team3= Team()
# print(Team1.TeamName)
# print(Team1.TeamOrigin)
# Team1.defineTeamName("Dolphin")
# print(Team1.TeamName)
# Team1.defineTeamOrigin("Nigeria")
# print(Team1.TeamOrigin)
# print(Team2.TeamName)
# print(Team2.TeamOrigin)
# print(Team3.TeamName)
# print(Team3.TeamOrigin)


# Inheritance of a Class
# class Team:
#     def __init__(self, Name="Name", Origin="Origin"):
#         self.TeamName = Name
#         self.TeamOrigin = Origin
#     def defineTeamName(self, Name):
#         self.TeamName = Name
#     def defineTeamOrigin(self, Origin):
#         self.TeamOrigin = Origin

# # class InheritanceClassName(ParentClass):
# #     def __init__(self, input1, input2):
# #         ParentClass.__init__(self)
# #         self.Attribute1 = input1
# #         self.Attribute2 = input2
# #         self.Attribute3 = 0

# class Player(Team):
#     def __init__(self):
#         Team.__init__(self)
#         self.PlayerName="None"
#         self.PlayerPoints=0


#     def scorePoint(self):
#         self.PlayerPoints +=1

#     def setName(self, Name):
#         self.PlayerName = Name
    
#     def __str__(self):
#         return self.PlayerName +" has scored: " + str(self.PlayerPoints) + " Points"


# player1 = Player()

# print(player1.PlayerName)
# print(player1.PlayerPoints)
# print(player1.TeamName)
# print(player1.TeamOrigin)
# player1.scorePoint()
# print(player1.PlayerPoints)
# player1.defineTeamName("Super Eagle")
# print(player1.TeamName)
# player1.setName("John")
# print(player1)

# PETS
class Pet:
    def __init__(self, n, a, h, p):
        self.name = n
        self.age  = a
        self.hunger = h
        self.playful = p 
# getters
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful

#setters
    def setName(self,name):
        self.name = name

    def setAge(self,age):
        self.age = age

    def setHunger(self,hunger):
        self.hunger = hunger

    def setPlayful(self,playful):
        self.playful = playful
    def __str__(self):
        return(self.name + "is "+str(self.age)+" years old")

class Dog(Pet):
    def __init__(self,name,age,hunger, playful,breed,ToyFavourite):
        Pet.__init__(self,name,age,hunger, playful)
        self.breed = breed
        self.ToyFavourite = ToyFavourite
    
    def wantsToPlay(self):
        if self.playful == True:
            return("Dog want to play with "+ self.ToyFavourite)
        else:
            return("Dog doesn't want to play")

class Cat(Pet):
    def __init__(self,name,age,hunger,playful,place):
        Pet.__init__(self,name, age,hunger,playful)
        self.FavouritePlaceToSit = place

    def wantsToSit(self):
        if self.playful==False:
            print("Cat want to sit on the", self.FavouritePlaceToSit)
        else:
            print("Cat doesn't want to play")
    def __str__(self):
        return(self.name +" likes to sit on "+self.FavouritePlaceToSit)
class Human:
    def __init__(self,name,Pets):
       self.name = name
       self.Pets = Pets
    def HasPets(self):
        if len(self.Pets) != 0:
            return "Yes"
        else:
            return "No"

cluffyCat = Cat("cluffy",5,False,False,"table")
cluffyCat.wantsToSit()
print(cluffyCat)
huskDog = Dog("ScrollBall",8,False,True,"Grand","Stick")
play=huskDog.wantsToPlay()
print(play)
yourAverageHuma = Human("Alice",[huskDog,cluffyCat])
hasPet=yourAverageHuma.HasPets()
print(hasPet)
print(yourAverageHuma.Pets[0].name)


# pet1=Pet("Cat",4,"Yes","No")
# print(pet1.getName())
# print(pet1.getPlayful())
# pet1.setName("SrollBall")
# print(pet1.getName())
# pet1.name = "Cat"
# print(pet1.name)