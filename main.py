from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vector(self.x - o.x, self.y - o.y)

    def __mul__(self, z):
        return Vector(z * self.x, z * self.y)

    def __rmul__(self, z):
        return Vector(z * self.x, z * self.y)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)


class Solid:
    def __init__(self, x, y, mass, name='', color=(0, 0, 0), speed=Vector(0, 0), acceleration=Vector(0, 0)) -> None:
        self.position = Vector(x, y)
        self.mass = mass
        self.speed = speed
        self.acceleration = acceleration
        self.name = name
        self.color = color

    def __str__(self) -> str:
        return f'''
                X:{self.position.x} ;
                Y:{self.position.y} ;
                Mass:{self.mass} ;
                Speed:{self.speed};
                Acceleration:{self.acceleration};
                Name: {self.name};
                 '''

    def update(self, dt, objects, G) -> None:
        gravity_force = Vector(0, 0)
        for i in objects:
            if i.position != self.position:
                gravity_force += i.mass * self.mass * G / abs((self.position - i.position).get_length()) ** 3 * (
                        i.position - self.position)
        self.acceleration = gravity_force * (1 / self.mass)
        self.speed += self.acceleration * dt
        self.position += self.speed
