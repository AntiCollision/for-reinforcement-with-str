import logging as log
import requests

from .option import Serial

def ScenarioStart(ip:str, port:int):
    log.info("Scenario Start!")
    print("http://{0}:{1}/start".format(ip,port))
    result = requests.get("http://{0}:{1}/start".format(ip,port))
    log.info("Receive Data : [{0}]".format(result))
    return result
    
def ScenarioStop(ip:str, port:int):
    log.info("Scenario Stop!")
    print("http://{0}:{1}/stop".format(ip,port))
    result = requests.get("http://{0}:{1}/stop".format(ip,port))
    log.info("Receive Data : [{0}]".format(result))
    return result
    

def SerialMovement(ip:str, port:int, serial: Serial):
    log.info("request thaht Serial movemnet!")
    req = serial.dump()
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    print("request dump data is : [{0}]".format(req))
    result = requests.post("http://{0}:{1}/serial".format(ip,port), req, headers=headers)
    print("Receive Data : [{0}]".format(result))
    return result

def SerialMovementArray(ip:str, port:int, serial: [Serial]):
    log.info("request thaht Serial movemnet!")
    req = "["
    req += ",".join(list(map(lambda x: x.dump(), serial)))
    req += "]"

    headers = {'Content-Type': 'application/json; charset=utf-8'}

    print("request dump data is : [{0}]".format(req))
    result = requests.post("http://{0}:{1}/serial_array".format(ip,port), req, headers=headers)
    print("Receive Data : [{0}]".format(result))
    return result
    
# def __receiver(udp, callback):
#     while True:
#         data, addr = udp.recvfrom(1024)
#         log.info("{0} -> {1}", addr, data.decode('utf-8'))
#         callback(data.decode('utf-8'), addr)
# nmea callbacker
# recommend port value is 3000
def NmeaReceiver(ip: str, port: int): 
    log.info("Get the State!")
    print("http://{0}:{1}/state".format(ip,port))
    result = requests.get("http://{0}:{1}/state".format(ip,port))
    log.info("Receive Data : [{0}]".format(result))
    return result.content.decode('utf-8')
    # udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udp.bind(('0.0.0.0', port))
    # t = th.Thread(target=__receiver, args=(udp, callback))
    # t.start()
