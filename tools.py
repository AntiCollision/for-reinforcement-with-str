import net
from option import Option, Serial
import logging as log
import datetime as dt
import time

data = []

def callback(rawdata, addr):
    data.append((dt.datetime.now(), rawdata))
        
class Tools:
    def __init__(self, opt:Option) -> None:
        self.opt = opt
        net.NmeaReceiver(self.opt.getStrNMEAPort(), callback)
    
    def Start(self):
        net.ScenarioStart(self.opt.getStrIP(), self.opt.getStrMacroPort())
        time.sleep(20)

    def Stop(self):
        net.ScenarioStop(self.opt.getStrIP(), self.opt.getStrMacroPort())
        time.sleep(15)
    
    def State(self) -> ([(dt.datetime, str)], int):
        global data
        copy = data
        data = []
        return (copy, len(copy))

    def Action(self, joy: [Serial]):
        for item in joy:
            log.info("Joystick Move : [%s]".format(item.dump()))
            net.SerialMovement(self.opt.getStrIP(), self.opt.getStrMacroPort(), item)        
