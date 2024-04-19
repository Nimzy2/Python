class MyStr:
    def __init__(self, my_string):
       self.my_string = my_string

    def my_lower(self):
        return self.my_string.lower()
    
    def my_upper(self):
        return self.my_string.upper()


name_1 = MyStr("Nimoh") # instanciate an object called name that stores "Nimoh"
name_2 = MyStr("Olum")

print(name_1.my_lower())
print(name_1.my_upper())
print()
print(name_2.my_lower())
print(name_2.my_upper())



