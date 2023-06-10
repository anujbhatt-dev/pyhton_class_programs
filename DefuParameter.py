#Program to Demonstrate the Use of Default Parameters in Methods

class Sub:
    def __init__(self, Th="RM", Prog="Python"):
        self.t = Th
        self.p = Prog

    def Theory(self):
        print(f"Theory Subject is {self.t}")

    def Programming(self):
        print(f"Practical Subject is  {self.p}")

def main():
       
    s = Sub()
    s.Theory()
    s.Programming()
if __name__ == "__main__":
    main()
