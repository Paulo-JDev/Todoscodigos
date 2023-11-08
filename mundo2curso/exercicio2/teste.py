""" from turtle import *

speed(13)
bgcolor('#990000')
pensize(10)
penup()
goto(0, 50)
pendown()
circle(-120)
penup()
circle(-120, -60)
pendown()
pensize(5)
right(50)
circle(70, 55)
right(85)
circle(75, 58)
right(90)
circle(70, 55)
right(90)
circle(70, 58)"""
import datetime
n = (datetime.date.today().year,
     datetime.date.today().month,
     datetime.date.today().day)
print(f'{n[2]}/{n[1]}/{n[0]}')
