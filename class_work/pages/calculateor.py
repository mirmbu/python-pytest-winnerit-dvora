class Calculator:
    def __init__(self, x=1, y=1):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    #add with the parameters ware init by initializing the class
    def add(self):
        return self.x + self.y
