# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
# timmy.color('blue')
# timmy.left(200)
# timmy.forward(300)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.align = 'l'



print(table)