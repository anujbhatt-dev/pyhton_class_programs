# example of multiple object

class cource:
    name=""
    year=0
    
# object creation
cr1=cource()
cr2=cource()

#accessing attributes and assigning new values
cr1.name="MCA-I"
cr1.year=1
cr2.name="MCA-II"
cr2.year=2

print(f"Course Name : {cr1.name} year : {cr1.year}")

print(f"Course Name : {cr2.name} year : {cr2.year}")
