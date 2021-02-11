class Family():
    def disp1(self):
        print("SURNAME", "Sharma")


class Father(Family):

    def disp2(self):
        print("Father Name", "RAM")
        print("Occupation", "EMPLOYEE")


class Mother(Family):

    def disp3(self):
        print("Mothers name", "RAMA")
        print("Mother age", 34)


class child(Mother, Father):
    def Inform(self):
        print("These are the family details")
        self.disp1()
        self.disp2()
        self.disp3()


c1 = child()
c1.Inform()
