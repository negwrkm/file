class Main:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def print_hi(self):
       print(f"hello {self.name}")
    def __say_hi(self):
        print("hi")

class App(Main):
    def __init__(self,h_color):
        super().__init__("xander",23)
        self.h_color=h_color
    
    def print_hi(self):
        print(f"hi {self.h_color} man or weman")

    def c_h(self):
        print("this is child")
class Child(App):
    def print_hi(self):
        print("*******")

c=Child("red")
c.print_hi()