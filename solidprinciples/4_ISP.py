# Interface Segregation Principle
# Clients should not be forced to depend upon interfaces that they do not use.

######## Violation ############
class Shapes:
    def draw_circle(self):
        raise NotImplemented
       
    def draw_square(self):
        raise NotImplemented

class Circles(Shapes):
    
    def draw_circle(self):
        pass

    def draw_square(self):
        pass

# In the above example, we need to call an unnecessary method in the Circle class.    

######### Solution ###########
class Shape:

    def draw(self):
        return "Draw a shape"

class Circle(Shape):

    def draw(self):
        return "Draw a circle"

class Square(Shape):

    def draw(self):
        return "Draw a square" 

circle = Circle()
draw_circle = circle.draw()
print(draw_circle)   

square = Square()
draw_square = square.draw()
print(draw_square)




