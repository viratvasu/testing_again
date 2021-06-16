class Glove:
    def __init__(self,color):
        self.__color = color
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color = color
class Minion:
    def __init__(self,glove):
        self.__glove = glove
        self.color = "pink"
    def get_glove(self):
        return self.__glove
v_g = Glove("violet")
y_g = Glove("yellow")
b = Minion(y_g)
s_g = v_g
y_g.set_color(b.color)
print(b.get_glove().get_color())