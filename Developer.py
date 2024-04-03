






from  Humam import  Human
class Developer(Human):
    def __init__(self,name,age,yonalish):
        super().__init__(name,age)
        self.yonalish = yonalish

    def codeYozish(self):
        print("Dasturchi code yozmoqda")

    def cofee_ichish(self):
        print("Cofe ishich vaqti")
