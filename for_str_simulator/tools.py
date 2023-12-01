from .net import *
from .option import Option, Serial
import logging as log
import time
import json
import pynmea2
import re
from datetime import datetime

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
    try:
        return (time_converter(date), pynmea2.parse(text.replace(" ", "")))
    except:
        return None

def fil(obj):
    return obj != None

class Tools:
    def __init__(self, opt:Option) -> None:
        self.opt = opt
    
    def Start(self):
        ScenarioStart(self.opt.getStrIP(), self.opt.getStrMacroPort())
        time.sleep(15)

    def Stop(self):
        ScenarioStop(self.opt.getStrIP(), self.opt.getStrMacroPort())
        time.sleep(8)
    
    def State(self):
        par = json.loads(NmeaReceiver(self.opt.getStrIP(), self.opt.getStrMacroPort()))
        conv = map(lambda x: parse(x['time'], x['data']), par['log'])
        res = list(filter(fil, conv))
        return res

    # -1 ~ 1
    # Ludder 0 ~ 1000
    # Others : -1000 ~ 1000
    def Action(self, ludder: float = None, engineL: float = None, engineR: float = None):
        if ludder != None:
            item = Serial(4, int((ludder * 500) + 500))
            log.info("Joystick Move : [%s]".format(item.dump()))
            SerialMovement(self.opt.getStrIP(), self.opt.getStrMacroPort(), item)
            time.sleep(0.8)
        if engineL != None:
            item = Serial(6, int((engineL * 1000)))
            log.info("Joystick Move : [%s]".format(item.dump()))
            SerialMovement(self.opt.getStrIP(), self.opt.getStrMacroPort(), item)
            time.sleep(0.8)
        if engineR != None:
            item = Serial(8, int((engineR * 1000)))
            log.info("Joystick Move : [%s]".format(item.dump()))
            SerialMovement(self.opt.getStrIP(), self.opt.getStrMacroPort(), item)
            time.sleep(0.8)
