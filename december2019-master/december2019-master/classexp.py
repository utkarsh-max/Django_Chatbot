class Computer:

    def config(self,speak):
        self.speak=speak
        print("Ram-2GB HDD-500GB")
    def __init__(self,cpu):
        self.cpu=cpu
        print("This is techSrijan |Computer",self.cpu)
    def speaker(self):
        print(self.speak)

p1=Computer("Dual Core")
p1.config("5W")
p2=Computer(" Core I3")
p2.config("10w")
p1.speaker()
#Computer.config(p1)