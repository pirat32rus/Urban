import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
        
    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed
            
    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")
        
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")
            
    def speak(self):
        print(self.sound)
        
class Bird(Animal):
    beak = True
    
    def lay_eggs(self):
        num_eggs = random.randint(1, 4)
        print(f"Here are(is) {num_eggs} eggs for you")
        
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 7
    
    def dive_in(self, dz):
        dz = abs(dz)
        
        speed_dive = self.speed / 2
        if self._cords[2] - dz * speed_dive >= 0:
            self._cords[2] -= dz * speed_dive
        else:
            print("It's too deep, i can't dive :(")
            
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in(6)
db.get_cords()

db.lay_eggs() 