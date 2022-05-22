class Car:

    current_speed = 0
    falling_speed = 0

    def __init__(self, title, model, hp, nm, weight, max_speed, color):
        self.title = title
        self.model = model
        self.hp = hp
        self.nm = nm
        self.weight = weight
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f"{self.title} {self.model} engine start!")

    def gas(self):
        self.current_speed += 20
        print(self.current_speed)

    def stoped_engine(self):
        print(f"{self.title} {self.model} engine stoped!")

    def tormoz(self):
        self.current_speed -= 20
        print(self.current_speed)

    def info(self):
        print(f""" 
              title:     {self.title} 
              model:     {self.model} 
              weight:    {self.weight} 
              hp:        {self.hp} 
              nm:        {self.nm} 
              max. speed:{self.max_speed} 
              color:     {self.color} 
                       """)



#Instance Car
bmw = Car("BMW", "x5 e53", 240, 470, 500, 270, "BLACK")
bmw.start_engine()
bmw.gas()
bmw.gas()
bmw.tormoz()
bmw.tormoz()
bmw.stoped_engine()
bmw.info()

mercedes = Car("Mercedes", "e63 //AMG", 300, 430, 700, 300, "WHITE")
mercedes.start_engine()
mercedes.gas()
mercedes.gas()
mercedes.tormoz()
mercedes.tormoz()
mercedes.stoped_engine()
mercedes.info()