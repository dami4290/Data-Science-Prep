import random

class Animal:
    def __init__(self, position, name, race_distance):
        self.position=position
        self.name=name
        self.race_distance=race_distance

    def move(self):
        ...
    def report_position(self):
        return self.position
    def has_finished(self):
        if self.position>=self.race_distance:
            return True
        else:
            return False
        
class Hare(Animal):
    def __init__(self, position, name, race_distance):
        super().__init__(position, name, race_distance)

    def move(self):
        x=random.randint(1,2)
        if x==1:
            distance=random.randint(5,10)
        else:
            distance=0
        self.position=distance+self.position
    
class Tortoise(Animal):
    def __init__(self, position, name, race_distance):
        super().__init__(position, name, race_distance)

    def move(self):
        distance=random.randint(1,5)
        self.position=distance+self.position

def main():
    race_distance=50
    hare=Hare(0, "Hare", race_distance)
    tortoise=Tortoise(0, "Tortoise", race_distance)
    while not hare.has_finished() and not tortoise.has_finished():
        hare.move()
        tortoise.move()
        print(hare.report_position())
        print(tortoise.report_position())
    if hare.has_finished() and tortoise.has_finished():
        print("It is a tie!!")
    elif hare.has_finished() and not tortoise.has_finished():
        print("Hare won!!")
    elif not hare.has_finished() and tortoise.has_finished():
        print("Tortoise won!!")

if __name__=="__main__":
    main()
    