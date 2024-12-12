class Poongu:
    def __init__(self,hobby,fav_food):
        self.hobby=hobby
        self.fav_food=fav_food
    def disp(self):
        print(f"Hobby:{self.hobby}\nFav_Food:{self.fav_food}")
class Shallz(Poongu):
    def __init__(self,fav_actor,ambition):
        self.fav_actor=fav_actor
        self.ambition=ambition
    def show(self):
        print(f"Fav_actor:{self.fav_actor}\nAmbition:{self.ambition}")
class Datchu(Poongu):
    def __init__(self,other_name_of_jk,sports):
        self.other_name_of_jk=other_name_of_jk
        self.sports=sports 
    def display(self):
        print(f"Names of jk:{self.other_name_of_jk}\nSports:{self.sports}")

class GeethaMam(Shallz,Poongu):
    def __init__(self,fav_actor,ambition,hobby,fav_food,degree):
        super().__init__(fav_actor,ambition)
        Poongu.__init__(self,hobby,fav_food)
        self.degree=degree
    def info(self):
        self.show()
        self.disp()
        print(f"Degree:{self.degree}")
a=GeethaMam("Adharvaa","Software developer","writting diary","everything","M.tech")
a.info()

class Student:
    def __init__(self,name,roll_no,tamil,eng,maths):
        self.name=name
        self.roll_no=roll_no
        self.tamil=tamil
        self.eng=eng
        self.maths=maths
    def show(self):
        print(f"Name:{self.name}\nRollNo:{self.roll_no}\nTamil Mark:{self.tamil}\nEng Mark:{self.eng}\nMaths Mark:{self.maths}")
class Total(Student):
    def display(self):
        total= self.tamil+self.eng+self.maths/300*100
        print("Percentage:",total)
s=Total("Poongu",12345,90,85,92)
s.show()
s.display()
                       





