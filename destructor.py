class stud:

    def nmprint(self):
        print(self.nm)
        print("example showing Constructor and destructor")
        
 # Initializing
    def __init__(self):
        self.nm = "Nihira"
        print("stud class created")
        
 # Calling destructor
    def __del__(self):
        print("Destructor called")
        
# creating object of the class
s = stud()
 
# calling the instance method using the object obj
s.nmprint()
del s

