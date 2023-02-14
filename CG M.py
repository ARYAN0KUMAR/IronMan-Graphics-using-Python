import turtle

import pygame

from time import sleep

piece1=[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20),
        (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]

piece2=[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210),
        (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]

piece3=[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250),
        (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]

piece4=[(-140, 10), (-40, -20),(-40, -30),(-50, -40), (-100, -46), (-130, -40),(-150,-26)]

piece5=[(140, 10), (40, -20),(40, -30),(50, -40), (100, -46), (130, -40),(150,-26)]

piece6=[(-130, 230), (-170, 200), (-186, -30), (-186, -40), (-120, -250),(-90, -280), (90, -280), (120, -250), (186, -40), (186, -30), (170, 200), (130, 230), (70, 260),
        (70, 620), (850, 620), (850, -620), (-850, -620), (-850, 620), (-70, 620), (70, 620), (70,260)]

pygame.mixer.init()

pygame.mixer.music.load('iron-man-3-theme.mp3')

pygame.mixer.music.play()

turtle.hideturtle()

turtle.bgcolor('#6a0c0b')

turtle.setup(1400,800)

turtle.title("IRONMAN")

sleep(5)

piece1Goto=(0,120)

piece2Goto=(0,-30)

piece3Goto=(0,-220)

piece4Goto=(-150,-10)

piece5Goto=(150, -10)

piece6Goto=(-70, 260)

turtle.speed(1)

def draw_piece(piece,pieceGoto):

   turtle.penup()

   turtle.goto(pieceGoto)

   turtle.pendown()

   turtle.color('#fab104')

   turtle.begin_fill()

   for i in range(len(piece)):

       x,y=piece[i]

       turtle.goto(x,y)

   turtle.end_fill()

   sleep(3)

draw_piece(piece1,piece1Goto)

draw_piece(piece2,piece2Goto)

draw_piece(piece3,piece3Goto)

turtle.speed(2)

def draw_piece(piece,pieceGoto):

   turtle.penup()

   turtle.goto(pieceGoto)

   turtle.pendown()

   turtle.color('white')

   turtle.begin_fill()

   for i in range(len(piece)):

       x,y=piece[i]

       turtle.goto(x,y)

   turtle.end_fill()

   sleep(1)

sleep(2)

draw_piece(piece4,piece4Goto)

draw_piece(piece5,piece5Goto)

turtle.speed(5)

turtle.penup()

turtle.goto(piece6Goto)

turtle.pendown()

turtle.color('black')

turtle.begin_fill()

for i in range(len(piece6)):

  x,y=piece6[i]

  turtle.goto(x,y)

turtle.end_fill()

turtle.hideturtle()

turtle.done()

