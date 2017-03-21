
class Animal:
    """Some properties of animals"""
    is_alive = True
    is_big = "Yes"
    is_carnivores = True
    domestic_animal = "Yes"

    def info(self):
        print("Alive = {}, Big = {}, Carnivores = {} , Domestic animal = {} "
              .format(self.is_alive, self.is_big, self.is_carnivores, self.domestic_animal))

    def voice(self,name, is_voice):
        self.name = name
        self.is_voice = is_voice
        if is_voice != True:
            print("{} has no voice".format(name))
        else:
            print("{} has voice".format(name))


Cat = Animal()
Cat.is_carnivores = False
Cat.is_big = "No"
Cat.info()
Cat.voice("Cat","No")

Wolf = Animal()
Wolf.domestic_animal = "No"
Wolf.info()
Wolf.voice("Wolf",True)



