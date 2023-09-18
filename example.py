from tools import *
import time
import random as rd
t = Tools(opt=Option("210.107.245.152", 7005, 3333, "-", 0))
t.Stop() 
t.Start()

for _ in range(1000):
    data = int(rd.random() * 2000) - 1000
    print(t.State())
    t.Action(joy=[Serial(4, data)])
    time.sleep(1)
    
t.Stop()