from turtle import *
from time import sleep
speed(10)

#red section
color('red')
begin_fill()
for i in range(2):
    fd(125)
    rt(90)
    fd(125)
    rt(90)
end_fill()

#white cross
color('white')
begin_fill()
pu()
goto(50, -50)
pd()
for i in range(4):
    lt(90)
    fd(25)
    rt(90)
    fd(25)
    rt(90)
    fd(25)
end_fill()

sleep(10)