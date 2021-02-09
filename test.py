class Demo:
    def __init__(self,name):
        self.name = name
    def printname(self):
        print('the name is the',self.name)
if __name__ == '__main__':
    Demo('hank moody karen').printname()
