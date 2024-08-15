from .net import *
from .option import Option, Serial
import logging as log
import time
import json
import pynmea2
import re
from datetime import datetime

RUDDER_CHOICES = [ 114, 154, 205, 256, 307, 358, 409, 460, 511, 562, 613, 664, 716, 767, 818, 869, 910 ]
ENGINE_CHOICES = [ 0, 205, 307, 409, 512, 613, 716, 818, 912, 1023 ]

# def callback(rawdata, addr):
#     data.append((dt.datetime.now(), rawdata))
        
def time_converter(x):
    # Extract numeric values and month string using regular expressions
    matches = re.findall(r'\w+', x)

    # Define a mapping between Go month names and Python month names
    month_mapping = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }

    # Replace the month string with its numeric representation
    matches[4] = str(month_mapping.get(matches[4], 1))
    def fil(x):
        try:
            int(x)
            return True 
        except:
            return False


    matches = list(filter(fil, matches))
    # Convert the list of strings to a list of integers
    numeric_values = list(map(int, matches))
    # Create a Python datetime object
    numeric_values[-1] = int(numeric_values[-1] / 1000)
    python_date = datetime(*numeric_values)
    return python_date.timestamp()


def parse(date, text):
    return (time_converter(date), text.split(','))

def fil(obj):
    return obj != None

class Tools:
    def __init__(self, opt:Option) -> None:
        self.opt = opt
    
    def Start(self):
        ScenarioStart(self.opt.getStrIP(), self.opt.getStrMacroPort())
        time.sleep(7)

    def Stop(self):
        ScenarioStop(self.opt.getStrIP(), self.opt.getStrMacroPort())
        time.sleep(2)
    
    def State(self):
        par = json.loads(NmeaReceiver(self.opt.getStrIP(), self.opt.getStrMacroPort()))
        conv = map(lambda x: parse(x['time'], x['data']), par['log'])
        res = list(filter(fil, conv))
        return res

    # -1 ~ 1
    # Ludder 0 ~ 1000
    # Others : -1000 ~ 1000
    def Action(self, rudder: int = None, engine: int = None):
        items = []
        
        if rudder != None:      # Rudder Angle 0 ~ 1023
            item = Serial(4, int(rudder))
            log.info("Joystick Move : [%s]".format(item.dump()))
            items.append(item)
            # SerialMovement(self.opt.getStrIP(), self.opt.getStrMacroPort(), item)
            # time.sleep(1) 
        if engine != None:     # Engine RPM 0 ~ 1023
            item = Serial(6, int(engine))
            log.info("Joystick Move : [%s]".format(item.dump()))
            items.append(item)
            # SerialMovement(self.opt.getStrIP(), self.opt.getStrMacroPort(), item)
            # time.sleep(1)
        SerialMovementArray(self.opt.getStrIP(), self.opt.getStrMacroPort(), items)
        time.sleep(0.05)
