import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x=x
        self.__y=y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        if self.__x>x:
            x=self.__x-x
        else:
            x=x-self.__x
        if self.__y>y:
            y=self.__y-y
        else:
            y=y-self.__y
            
        return math.hypot(x,y)
        
    def distance_from_point(self, point):
        if self.__x>point.getx():
            x=self.__x-point.getx()
        else:
            x=point.getx()-self.__x
        if self.__y>point.gety():
            y=self.__y-point.gety()
        else:
            y=point.gety()-self.__y
            
        return math.hypot(x,y)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points=[vertice1,vertice2,vertice3]

    def perimeter(self):
        return (self.__points[0].distance_from_point(self.__points[1]))+(self.__points[1].distance_from_point(self.__points[2]))+(self.__points[2].distance_from_point(self.__points[0]))


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
