class Testing:
    def __init__(self):
        self.x = 0

    def attendance(self):
        self.x = self.x + 1

    def __del__(self):
        print("Attendance cutoff")


class Absents:
    def __init__(self):
        self.x = 0

    def Absents2(self):
        self.x = self.x + 1
        print("=========================\nAbsents", self.x, "\n==========================")


an = Testing()
bn = Absents()


an.attendance()
an.attendance()
an.attendance()
an.attendance()
print(f"Present {an.x}")


bn.Absents2()

print("only", an.x, "is present")


