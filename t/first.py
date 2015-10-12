# coding:utf-8
__author__ = 'yinzishao'
# dic ={}

class operation():
    def GetResult(self):
        pass

class operationAdd(operation):
    def GetResult(self):
        return self.numberA + self.numberB

class operationDev(operation):
    def GetResult(self):
        if(self.numberB!=0):
            return self.numberA /self.numberB
        else:
            raise "被除数不能为0"

class operationMul(operation):
    def GetResult(self):
        return self.numberA*self.numberB

class operationSub(operation):
    def GetResult(self):
        return self.numberA-self.numberB

class operationFac():
    dic ={}
    def __init__(self):
        self.dic ={"+":operationAdd(),"-":operationSub(),"/":operationDev(),"*":operationDev()}
    def creatOpe(self,sign):
        if sign in self.dic:
            return self.dic[sign]
        else:
            return "faise"

if __name__ =="__main__":
    fuhao = raw_input("operator:")
    nA= input("a:")
    nB= input("b:")
    a =operationFac().creatOpe(fuhao)
    a.numberA=nA
    a.numberB=nB
    print a.GetResult()
    # dic ={"+":operationAdd(),"-":operationSub(),"/":operationDev(),"*":operationDev()}
    # print dic
