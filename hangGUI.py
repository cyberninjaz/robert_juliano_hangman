from turtle import Screen, Turtle
from tkinter import *
from math import sqrt
import hangmanmodel
from pynput import keyboard
from pynput.keyboard import Key
import turtle
import random
from alphabet import alphabet

canvas = Screen()
inp = simpledialog.askstring("Input", "What is your word?", parent=canvas.getcanvas())
hangmanmodel.start(inp)
canvas.setup(1000, 750, None, None)

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#ffffff")
myPen.pensize(2)

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 

#Main Program Starts Here
fontSize = 30
characterSpacing = 4
fontColor = "#000000"

message = None

def keyboardListener(key) :
    if hangmanmodel.guessL(str(key)[1]) :
        #displayMessage("testing", fontSize, fontColor, -190, 0)
        canvas.create_text(20, 30, anchor=W, font="Arial",text="YEET")
        #if guessL(str(key)) :

with keyboard.Listener(on_press=keyboardListener) as listener:
    t = Turtle()

    # Head
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(45)
    t.left(-90)

    #Body
    t.forward(180)

    # Body
    t.left(0.5*90)
    t.forward(100*sqrt(2))

    # Leg 1
    for i in range(4) :
        t.left(0.5*90)
    t.forward(100*sqrt(2))
    t.left(90)
    t.forward(100*sqrt(2))

    # Leg 2
    for i in range(4) :
        t.left(0.5*90)
    t.forward(100*sqrt(2))
    t.left(45)
    t.forward(90)
    t.left(90)

    # Arm 1
    t.forward(120)
    # Arm 2
    t.backward(240)
    t.penup()
    t.goto(-575, -300)
    for i in range(4) :
        t.left(0.5*90)

    # Letters
    for i in range(len(inp)) :
        t.pendown()
        t.forward(50)
        t.penup()
        t.forward(25)
    
    # canvas.exitonclick()
    listener.join()
    
