#coding=utf-8
"""工厂方法模式 把实例化延续到之类中创建,这样的话增加某些功能就不用往之前的核心工厂类添加代码"""
__author__ = 'yinzishao'
class Leifeng():
    def sweep(self):
        print "做好事"

class Student(Leifeng):
    def sweep(self):
        print "学生做好事"

class Volunteer(Leifeng):
    def sweep(self):
        print "志愿者做好事"

class AbstractFactory():
    def creatLeifeng(self):
        temp =Leifeng()
        return temp
class StudentFactory(AbstractFactory):
    def creatLeifeng(self):
        return Student()
class VolunteerFactory(AbstractFactory):
    def creatLeifeng(self):
        return Volunteer()

if __name__ =="__main__":
    af = VolunteerFactory()
    leifeng = af.creatLeifeng()
    leifeng.sweep()
