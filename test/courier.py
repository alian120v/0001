from turtle import distance


spart=(0,0)
class XY:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"x= {self.x}, y= {self.y} "
    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
class courier(XY):
    def __init__(self,x,y,v,name_courier):
        XY.__init__(self,x,y)
        self.v=v
        self.name_courier = name_courier
    def __str__(self):
        return f'x= {self.x}, y= {self.y}, имя курьера {self.name_courier}, его скорость {self.v}'
    def time(self, other):
        return (2*(self.distance(other)))/self.v
p1=XY(2,2)
cour1=courier(2,3,3,'Ivan')
dis=p1.distance(cour1)
t=cour1.time(p1)
print(dis)