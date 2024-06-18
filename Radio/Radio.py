class Radio:
    def __init__(self) -> None:
        self.powerStatus = False
        self.volume = 0
        self.frequency = 0

    def volumeUp(self):
        self.volume += 1
    
    def volumeDown(self):
        self.volume -= 1

    def turnOn(self):
        self.powerStatus = True

    def turnOff(self):
        self.powerStatus = False

    def choseSender(self, frequency):
        self.frequency = frequency
