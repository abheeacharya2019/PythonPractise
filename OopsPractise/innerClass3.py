class Human:
    def __init__(self):
        self.name = "Abhishek"
        self.head = self.Head()
        self.mouth = self.Mouth()

    def display(self):
        print("Name : ", self.name)

    class Head:
        def think(self):
            print("Thinking...")

    class Mouth:
        def talk(self):
            print("Talking...")


h = Human()
h.display()
h.head.think()
h.mouth.talk()
