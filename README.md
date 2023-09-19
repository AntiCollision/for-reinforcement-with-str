# for-reinforcement-with-str

## How to Install this program?

```sh
# This All!
$ python3 -m pip install https://github.com/AntiCollision/for-reinforcement-with-str.git
```

```py
from for_str_simulator import *
import time
import random as rd

t = Tools(opt=Option("STR Macro IP", `Macro Port`, `DB Port`))
t.Start()

for _ in range(10):
    data = int(rd.random() * 2000) - 1000
    print(t.State())
    t.Action(joy=[Serial(4, data)])
    time.sleep(0.5)
    
t.Stop()
```

