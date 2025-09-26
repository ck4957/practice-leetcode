class Singleton:
    
    def __init__(self):
        if Singleton.__instance:
            return Singleton.__instance
        Singleton.__instance = self

a = Singleton()
b = Singleton()
print(a is b)  # True
