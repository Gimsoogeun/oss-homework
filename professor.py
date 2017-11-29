

class professor:
    name=''
    number=0
    __lectures=[]
    def __init__(self,name,number):
        self.name=name
        self.number=number

    def enrollCourse(self,lec):
        self.__lectures.append(lec)

    def printCourse(self):
        for i in range(len(self.__lectures)):
            print(self.__lectures[i])

hong=professor('홍길동',12345678)
hong.enrollCourse('공개SW실무')
hong.enrollCourse('웹프로그래밍')
hong.printCourse()
