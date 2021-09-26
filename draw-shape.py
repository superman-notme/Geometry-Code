import turtle 
sides = int(input("How many sides would you like"))
angle = 360 / sides
print(angle)


def draw_shape():
  for i in range(0, sides):
    turtle.fd(20)
    turtle.lt(angle)
draw_shape()
