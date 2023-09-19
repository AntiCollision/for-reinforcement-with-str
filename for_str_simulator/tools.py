import net
from option import Option, Serial
import logging as log
import datetime as dt
import time
import json
import pynmea2


# def callback(rawdata, addr):
#     data.append((dt.datetime.now(), rawdata))
        
def parse(date, text):
    try:
        return (date, pynmea2.parse(text.replace(" ", "")))
    except:
        return None

def fil(obj):
    return obj != None

class Tools:
    def __init__(self, opt:Option) -> None:
        self.opt = opt
    
    def Start(self):
        net.ScenarioStart(self.opt.getStrIP(), self.opt.getStrMacroPort())
        time.sleep(15)

    def Stop(self):
        net.ScenarioStop(self.opt.getStrIP(), self.opt.getStrMacroPort())
        time.sleep(8)
    
    def State(self):
        par = json.loads(net.NmeaReceiver(self.opt.getStrIP(), self.opt.getStrMacroPort()))
        conv = map(lambda x: parse(x['time'], x['data']), par['log'])
        res = list(filter(fil, conv))
        return res

    def Action(self, joy: [Serial]):
        for item in joy:
            log.info("Joystick Move : [%s]".format(item.dump()))
            net.SerialMovement(self.opt.getStrIP(), self.opt.getStrMacroPort(), item)        