import random
import turtle
okragx = []
okragy = []
kwadratx = []
kwadraty = []
window = turtle.Screen()
turtle.setworldcoordinates(-1, -1, 1, 1)
turtle.up()
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0, 0)
iter = int(input("Podaj Liczbe Iteracji: "))
x = int(input("Po ile kropek ma wstawiac: "))
def main():
    for i in range(iter):
        rx = random.uniform(-1, 1)
        ry = random.uniform(-1, 1)
        if (rx**2) + (ry**2) <= 1:
            okragx.append(rx)
            okragy.append(ry)
            turtle.setx(rx)
            turtle.sety(ry)
            turtle.dot(3, "green")
        else:
            kwadratx.append(rx)
            kwadraty.append(ry)
            turtle.setx(rx)
            turtle.sety(ry)
            turtle.dot(3, "red")
        pi = 4*(len(okragx)/(len(okragx)+len(kwadratx)))
        print(pi)
        if i % x == 0:
            turtle.update()
    input("Koniec...")
    window.exitonclick()
main()