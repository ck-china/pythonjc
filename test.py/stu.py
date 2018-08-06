class Stu(object):
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getScores(self):
        return (self.scores)
a=Stu('ll',14,[90,80,70])
print(a.getName())
print(a.getAge())
print(a.getScores())
