import turtle
import  Osztaly

ablak = turtle.Screen()
ablak.title("Pontverseny")
ablak.bgcolor("black")


def kilepes():
    ablak.bye()

pont1 = Osztaly.MozgoPont("cyan", -200, 0, 15)
pont2 = Osztaly.MozgoPont("magenta", -200, 50, 10)
pont3 = Osztaly.MozgoPont("green", -200, 100, 20)

ablak.listen()

ablak.onkey(kilepes, "Escape")
ablak.onkey(pont1.inditas, "d")
ablak.onkey(pont2.inditas, "k")
ablak.onkey(pont3.inditas, "l")

turtle.mainloop()