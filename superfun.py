#Program 11.17: Program to Demonstrate the Use of super() Function

class Insti:
    def __init__(self, InstNm):
        self.Inm = InstNm
    def Inst_info(self):
        print(f"Institute is {self.Inm}")
class mcaInst(Insti):
    def __init__(self, InstNm, area):
        super().__init__(InstNm)
        self.ar = area
    def info(self):
        print(f"Best Institute for MCA {self.Inm} and is in {self.ar} ")
def main():
    I = mcaInst("DYPIMR", "Pimpri")
    I.info()
    I.Inst_info()
if __name__== "__main__":
    main()





    
