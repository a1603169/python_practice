class aoi:

    def __init__(self, name):
        self.name = name
        print('initialized')

    def hello(self):
        print("hello" + (self.name))

    def goodbye(self):
        print("goodbye" + (self.name))


m = aoi("aoi")
m.hello()
m.goodbye()
print(m)
