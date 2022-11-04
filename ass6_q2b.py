class Dog:
  def __init__(self,name,age,coatColor):
    self.name = name 
    self.age = age 
    self.coatColor = coatColor

  def description(self):
    print("Dog's name : ",self.name)  
    print("Dog's age : ",self.age)  

  def getinfo(self):
    print("coatColor : ",self.coatColor)

class JackRussellTerrier(Dog):
  def __init__(self,name,age,coatColor,height,weight):
    super().__init__(name,age,coatColor) 
    self.height = height
    self.weight = weight  

  def heightjack(self):
    print("height : ",self.height) 


  def weightjack(self):
    print("weight : ",self.weight)


class Bulldog(Dog):
  def __init__ (self,sex,training_status,name,age,coatColor):
    super().__init__(name,age,coatColor)
    self.sex = sex
    self.training_status = training_status


  def identity(self):
    print("sex : ",self.sex) 

  def training(self):
    print("training statues  : ",self.training_status) 




dogy = Dog("Mickel",2,"Brown")  
dogy.description()
dogy.getinfo()
dg = JackRussellTerrier("Mongo",4,"Black",3,25) 
dg.heightjack()
dg.weightjack()
dg.getinfo()
bull = Bulldog('masculine','trained','bulldog',6,'white')
bull.identity()
bull.training()
bull.getinfo()