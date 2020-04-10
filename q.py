class Hexagon():
    def __init__(self, radius):
        self.radius = radius

    def caculate_area(self):
        return self.radius * 6

a_hexagon =Hexagon(6)
print(a_hexagon.caculate_area())
