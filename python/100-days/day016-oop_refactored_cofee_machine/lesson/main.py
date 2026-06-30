# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.field_names = ["Pokemon Name", "Type"]
my_table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
my_table.align = "l"



print(my_table)
