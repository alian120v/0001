class XY:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"x= {self.x}, y= {self.y} "
    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
class courier(XY):
    def __init__(self,x,y,v,name):
        XY.__init__(self,x,y)
        self.v=v
        self.name = name
    def __str__(self):
        return f'x= {self.x}, y= {self.y}, имя курьера {self.name_courier}, его скорость {self.v}'
    def time(self, other):
        return (2*(self.distance(other)))/self.v
class order(XY):
    def __init__(self,x,y,name):
        XY.__init__(self,x,y)
        self.name = name
or1=order(0,5,'1')
or2=order(0,3,'2')
cour1=courier(0,0,3,'Ivan')
print(or1.distance(0,0))