from turtle import Screen, Turtle
from random import randint

s = Screen()
s.setup(560,560)
s.title("A drunken turtle collecting ...")

s.tracer(False)
writer = Turtle(visible=False)
writer.penup()
writer.goto(0, -275)

coins = []
for i in range(-4,5):
  for j in range(-4, 5):
      if i == j == 0:
          continue
      c = Turtle(shape="circle")
      c.color("", "orange")
      c.shapesize(0.5)
      c.goto(40*i, 40*j)
      coins.append(c)
s.tracer(True)

DRUNKENNESS = 45       
t = Turtle(shape="turtle")
t.color("black","")
points = 0
while abs(t.xcor()) < 200 and abs(t.ycor()) < 200:
  t.forward(5)
  t.right(randint(-DRUNKENNESS, DRUNKENNESS))
  found = None
  for c in coins:
      if t.distance(c) < 10:
          found = c
          break
  if found:
      found.hideturtle()
      coins.remove(found)
      t.shapesize(1+points/5., outline=1+points)
      points += 1

writer.write("{0} points".format(points),
           align="center", font=('Arial', 24, 'bold'))