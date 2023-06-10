#Program to Illustrate the Creation of Multiple Objects for a Class
class Games:
    def __init__(self, gname):
        self.gname = gname

    def indoor(self):
        print(f"{self.gname} Chess")

    def outdoor(self):
        print(f"{self.gname} Hockey - National Game of India")

def main():
    g = Games("Indoor game")
    i = Games("Brainy Game")
    o = Games("Outdoor")
    g.indoor()
    i.indoor()
    o.outdoor()

if __name__ == "__main__":
    main()

