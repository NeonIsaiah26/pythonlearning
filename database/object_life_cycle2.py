class Testing:
    def __init__(self):
        self.x = 0

    def attendance(self):
        self.x = self.x + 1

    def __repr__(self):
        return "Ito as object ng Testing"

    def __del__(self):
        print("Attendance cutoff")


class Absents:
    def __init__(self):
        self.x = 2

    def __repr__(self):
        return "Ito as object ng Absents"

    def Absents2(self):
        self.x = self.x + 1
        print("=========================\nAbsents", self.x, "\n==========================")


if __name__ == "__main__":

    an = Testing()
    bn = Absents()


    an.attendance()
    an.attendance()
    an.attendance()
    an.attendance()
    print(f"Present {an.x}")


    bn.Absents2()

    print("only", an.x, "is present")


