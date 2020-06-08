class Hashing:

    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def generateHashfunction(self, key):
        h=0
        for char in key:
            h+= ord(char)
        return h%self.MAX

    # def add(self,key,value):
    #     h=self.generateHashfunction(key)
    #     self.arr[h]=value
    #
    # def get(self,key):
    #     h = self.generateHashfunction(key)
    #     return self.arr[h]

    def __setitem__(self, key, value):
        h=self.generateHashfunction(key)
        self.arr[h]= value

    def __getitem__(self, item):
        h=self.generateHashfunction(item)
        return self.arr[item]





gh= Hashing()
print(gh.generateHashfunction("march 6"))
print(gh.generateHashfunction("march 17"))

# gh.add("march 6",330)
# print(gh.get("march 6"))

gh["march 6"]=450

print(gh.arr)

