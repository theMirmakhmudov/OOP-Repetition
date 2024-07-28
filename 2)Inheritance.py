# Yangi klasslar ota klasslardan meros oladi.  # noqa
# https://github.com/theMirmakhmudov
# https://youtube.com/@Mirmakhmudov_coder # noqa

# Father class
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Inheritance class
class SweetFruit(Fruit):
    def __init__(self, name, color, taste, tip):
        super().__init__(name, color)  # Father class call the constructor
        self.taste = taste
        self.tip = tip

    def show_display(self):
        return f"This fruit's name is {self.name}. It's {self.taste} and {self.tip}."

# SweetFruit create object
apple = SweetFruit("apple", "red", "sweet", "delicious")

# show result
print(apple.show_display())  # This fruit's name is apple. It's sweet and delicious.

