class Testing:
    def __init__(self):
        self.x = 0

    def attendance(self):
        self.x = self.x + 1
        print("Present", self.x)
an = Testing()

print("Type: \n", type(an))
print("\nDir: \n", dir(an))
print("\nType: \n", type(an.x))
print("\nType: \n", type(an.attendance))