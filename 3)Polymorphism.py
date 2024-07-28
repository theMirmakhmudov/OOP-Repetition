# Bir metod bir necha turdagi obyektlar bilan ishlaydi.  # noqa
# https://github.com/theMirmakhmudov
# https://youtube.com/@Mirmakhmudov_coder # noqa

# Father class
class Pen:
    def __init__(self, color, price, brand):
        self.color = color
        self.price = price
        self.brand = brand

    # method
    def show_info(self):
        return f"This pen's color is {self.color}\nThis pen's price is {self.price}\nThis pen's brand is {self.brand}"

# Inheritance class
class RedPen(Pen):
    def __init__(self, color, price, brand, thickness):
        super().__init__(color, price, brand)
        self.thickness = thickness
    # Polymorphism
    def show_info(self):
        return f"This pen's color is {self.color}\nThis pen's price is {self.price}\nThis pen's brand is {self.brand}\nThis pen's thickness is {self.thickness}"

# result function for show the difference
def show_result(pen_info):
    print(pen_info.show_info())

pen = Pen("blue","1$","Lamy")
red_pen = RedPen("red","2$","Pilot","1.2mm")

show_result(pen)
print("----------------------------------------")
show_result(red_pen)
