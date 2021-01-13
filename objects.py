class Cat():
    def __init__(self, color='red', age=0):
        self.color = color
        self.age = age

    def bark(self, text='myu'):
        print(text)


anfisa = Cat(color='blue', age=-10)
anfisa.bark()
gosha = Cat('white', 36)
print(anfisa)
