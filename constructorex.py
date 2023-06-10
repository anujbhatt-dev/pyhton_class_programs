class stud:
     
    def nmprint(self):
        print(self.nm)
        print("example of Contructor")
 
 # default constructor
    def __init__(self):
        self.nm = "Nihira"
 
# creating object of the class
s = stud()
 
# calling the instance method using the object obj
s.nmprint()


