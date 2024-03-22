import math


class Shape:
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if not (
            self.a + self.b > self.c
            and self.a + self.c > self.b
            and self.b + self.c > self.a
        ):
            raise ValueError("Not a triangle")

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)


def compute_area(*args, **kwargs):
    if len(args) == 1:
        return Circle(*args).get_area()
    elif len(args) == 3:
        return Triangle(*args).get_area()
    else:
        raise ValueError("Wrong number of arguments")


if __name__ == "__main__":
    pass
