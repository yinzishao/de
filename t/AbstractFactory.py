#coding=utf-8
""" 抽象工厂模式  创建一系列产品
    sql与access 工厂 分别创建 各自的方法
"""
__author__ = 'yinzishao'

class IUser():
    def InsertUser(self):
        pass
    def GetUser(self):
        pass

class IDepartment():
    def InsertDepartment(self):
        pass
    def GetDepartment(self):
        pass

class SqlUser(IUser):
    def InsertUser(self):
        print "sqluser"
    def GetUser(self):
        print "sqlgeruser"

class AccessUser(IUser):
    def InsertUser(self):
        print "accessuser"

    def GetUser(self):
        print "accessgetuser"

class SqlDepartment(IDepartment):
    def InsertDepartment(self):
        print "sqldepartment"
    def GetDepartment(self):
        print "sqlgerdepartment"

class AccessDepartment(IDepartment):
    def InsertDepartment(self):
        print "accessIdepartment"
    def GetDepartment(self):
        print "accessGetDepartment"

class Factory():
    def creatUser(self):
        pass
    def creatDepartment(self):
        pass

class sqlFac(Factory):
    def creatUser(self):
        temp = SqlUser()
        return temp
    def creatDepartment(self):
        return SqlDepartment()

class accessFac(Factory):
    def creatUser(self):
        return AccessUser()
    def creatDepartment(self):
        return AccessDepartment()
#使用简单工厂方法和反射来简化抽象工厂
class DataAccess():
    pass

if __name__ == "__main__":
    fac = accessFac()
    sqlu =fac.creatUser()
    sqlu.InsertUser()
