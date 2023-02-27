class employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name
    
    def name_fuc(self):
        print(self.id, self.name)

obj = employee("Yash", 1)

obj.name = "Yash"
obj.id = 1

del obj.id

obj.id = 2

obj.name_fuc()