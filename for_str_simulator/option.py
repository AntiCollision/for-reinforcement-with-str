import logging as log
import json

class Option:
    def __init__(self, str_ip:str, str_macro_port:int, db_port:int):
        log.info("create that option object")
        self.str_ip = str_ip
        self.str_macro_port = str_macro_port
        # self.str_nmea_port = str_nmea_port
        self.db_port = db_port

    def getStrIP(self) -> str:
        return self.str_ip
    
    def getStrMacroPort(self) -> int:
        return self.str_macro_port
    
    # def getStrNMEAPort(self) -> int:
        # return self.str_nmea_port
    def getDatabasePort(self) -> int:
        return self.db_port
    
# $"{{\"type\":4,\"id\":0,\"value\":{_ludder}}}",
# $"{{\"type\":6,\"id\":0,\"value\":{_engineL}}}",
# $"{{\"type\":8,\"id\":0,\"value\":{_engineR}}}"
# https://github.com/AntiCollision/SSvJoy-PC
# {"type":3, "id":1,"value":1023}
class Serial:
    def __init__(self, type: int, value: int) -> None:
        self.type = type
        self.value = value
    
    def dump(self) -> str:
        return json.dumps({"type":self.type,"id":0,"value":self.value}, separators=(',', ':'))