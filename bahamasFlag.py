from turtle import *
from time import sleep

#top third
color('deepskyblue')
begin_fill()
for i in range(2):
    fd(200)
    rt(90)
    fd(40)
    rt(90)
rt(90)
fd(40)
lt(90)
end_fill()

#middle third
color('yellow')
begin_fill()
for i in range(2):
    fd(200)
    rt(90)
    fd(40)
    rt(90)
rt(90)
fd(40)
lt(90)
end_fill()

#bottom third
color('deepskyblue')
begin_fill()
for i in range(2):
    fd(200)
    rt(90)
    fd(40)
    rt(90)
rt(90)
fd(40)
rt(180)
end_fill()

#black triangle
color('black')
begin_fill()
fd(120)
rt(120)
fd(120)
rt(120)
fd(120)
end_fill()

sleep(10)