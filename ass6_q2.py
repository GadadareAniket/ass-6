class Dog:

  def __init__(self,name,age,coatColour):
    self.name=name
    self.age=age
    self.coatColour=coatColour

  def description(self):
    print("Name: ",self.name )
    print("Age: ",self.age)

  def get_info(self):
    print("Coat Colour: ",self.coatColour)

class JackRussellTerrier(Dog):
  def __init__(self,name,age,coatColour,gender,breed):
    self.gender=gender
    self.breed=breed
    super().__init__(name, age, coatColour)
  
  def sex(self):
    print("Gender: ",self.gender)

  def variety(self):
    print("Breed: ",self.breed)

class Bulldog(Dog):
  def __init__(self,name,age,coatColour,origin,height):
    self.origin=origin
    self.height=height
    super().__init__(name, age, coatColour)

  def country(self):
    print("Origin: ",self.origin)

  def physique(self):
    print("Height: ",self.height)



obj=JackRussellTerrier("Aishu",2,"White","female","Labrador")
obj.description()
obj.get_info()
obj.sex()
obj.variety()

obj1=Bulldog("Aishu",2,"White","England","4 feet")
obj1.description()
obj1.get_info()
obj1.country()
obj1.physique()