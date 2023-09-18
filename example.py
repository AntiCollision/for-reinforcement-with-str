from tools import *
import time
import random as rd

t = Tools(opt=Option("210.107.245.190", 7000, 3333, "-", 0))
t.Start()

for _ in range(10):
    data = int(rd.random() * 2000) - 1000
    print(t.State())
    t.Action(joy=[Serial(4, data)])
    time.sleep(0.5)
    
t.Stop()