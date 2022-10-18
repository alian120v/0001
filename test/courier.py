class XY:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"x= {self.x}, y= {self.y} "
    def distance(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
class order:
    def __init__(self,x,y,name_courier):
        self.x=x
        self.y=y
        self.name_courier = name_courier
    def __str__(self):
        return f'x= {self.x}, y= {self.y}, имя курьера работуюшего над заказом {self.name_courier}'
p1=XY(2,2)
p2=XY(0,1)
ord=order(2,3,'Ivan')
dis=p1.distance(p2)
print(ord)