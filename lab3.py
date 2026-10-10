# class Rectangle:
#     default_color = 'greeen'

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height




# rectangle = Rectangle(10, 20)
# print(rectangle)
# print(rectangle.area())


# class MyClass:
#     @staticmethod
#     def ex_static_method():
#         print('static method')

#     @classmethod
#     def ex_class_method(cls):
#         print('class method')

#     def some_method(self):
#         print('my method')



# myclass = MyClass()


# class Vektor:

#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def addition(self, other):
#         x1 = self.x + other.x
#         y1 = self.y + other.y
#         z1 = self.z + other.z
#         new_vector = Vektor(x1, y1, z1)
#         return new_vector

#     def difference(self, other):
#         x1 = self.x - other.x
#         y1 = self.y - other.y
#         z1 = self.z - other.z
#         new_vector = Vektor(x1, y1, z1)
#         return new_vector

#     def scalar_multiple(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result

#     def __str__(self):
#         return(f' predstavlenie {self.x} and {self.y} and {self.y}')


# my_vector = Vektor(1,2,3)
# test_vector = Vektor(4,5,6)
# print(my_vector.addition(test_vector))











