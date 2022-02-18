import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, direction):
        def init(self, direction):
            self.direction = direction

        if direction == 'right': self.x += 1
        if direction == 'left': self.x -= 1
        if direction == 'up': self.y += 1
        if direction == 'down': self.y -= 1

    def dist(self, point):
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)


print("X for point 1")
point1x = int(input())
print("Y for point 1")
point1y = int(input())
print("X for point 2")
point2x = int(input())
print("Y for point 2")
point2y = int(input())

point1 = Point(point1x, point1y)
point2 = Point(point2x, point2y)
#point1 = Point(2, 5) --> example
#point2 = Point(8, 6)

print("What operations? \n"
      "№ show points \n"
      "№ move points \n"
      "№ distance points \n")
operation = input()
if operation == "show":
    print("first point:")
    point1.show()
    print("second point:")
    point2.show()
elif operation == "move":
    print("where? \n"
          "input: right, left, up, down")
    point1.move(input())
    point1.show()
elif operation == "distance":
    print(point1.dist(point2))
