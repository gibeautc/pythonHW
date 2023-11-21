#!/bin/python

# Consider a table fan and implement a TableFan class. What would be the attributes of this
# class? Examples of attributes could be speed levels of the fan, side-to-side movement (on/off,
# and degrees of movement), manufacturer name, cost, etc. Think about it this way: you want
# to be able to get information about the fan; for example, if you want to buy or sell a fan on a
# website such as Craigslist, what features would you be interested in? Also, consider control
# (operations) you might want to have over the fan such as setting the speed or having it
# oscillate.
# The TableFan class should include at least three attributes and three methods.


class TableFan:
    speed=0 #0 is off, 10 is max
    oscillating=False
    def __init__(self) -> None:
        self.speed=0
        self.oscillating=False
    def stop(self):
        self.speed=0
    def getSpeed(self):
            return self.speed
    def setSpeed(self,speed):
        if speed>=0 and speed<=10:
            self.speed=speed
        else:
            print("invalid speed")
    def setOscillating(self,oscillate):
        self.oscillating=oscillate
    def printStatus(self):
        if self.speed==0:
            print("Fan OFF")
        else:
            print("Fan Speed:",self.speed," Ossilating:",self.oscillating)
    


if __name__=="__main__":
    fan=TableFan()
    fan.printStatus()
    fan.setSpeed(5)
    fan.printStatus()
    fan.setOscillating(True)
    fan.printStatus()
    fan.stop()
    fan.printStatus()