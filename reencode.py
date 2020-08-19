#!/usr/bin/env python3
import sys

if len(sys.argv) != 2: sys.exit(1)

fn = sys.argv[1]

with open(fn, 'r') as f:
    data = f.read()

data = data.replace("\U0001b302", "\U0001ba01")
data = data.replace("\U0001b303", "\U0001ba02")
data = data.replace("\U0001b304", "\U0001ba03")
data = data.replace("\U0001b305", "\U0001ba04")
data = data.replace("\U0001b307", "\U0001ba06")
data = data.replace("\U0001b308", "\U0001ba07")

data = data.replace("\U0001b311", "\U0001ba08")
data = data.replace("\U0001b312", "\U0001ba09")
data = data.replace("\U0001b313", "\U0001ba0a")
data = data.replace("\U0001b314", "\U0001ba0b")
data = data.replace("\U0001b315", "\U0001ba0c")
data = data.replace("\U0001b317", "\U0001ba0e")
data = data.replace("\U0001b318", "\U0001ba0f")

data = data.replace("\U0001b31e", "\U00000323")
data = data.replace("\U0001b31f", "\U00000305")

data = data.replace("1B302", "1BA01")
data = data.replace("1B303", "1BA02")
data = data.replace("1B304", "1BA03")
data = data.replace("1B305", "1BA04")
data = data.replace("1B307", "1BA06")
data = data.replace("1B308", "1BA07")

data = data.replace("1B311", "1BA08")
data = data.replace("1B312", "1BA09")
data = data.replace("1B313", "1BA0A")
data = data.replace("1B314", "1BA0B")
data = data.replace("1B315", "1BA0C")
data = data.replace("1B317", "1BA0E")
data = data.replace("1B318", "1BA0F")

data = data.replace("1B31E", "0323")
data = data.replace("1B31F", "0305")

data = data.replace("1b302", "1ba01")
data = data.replace("1b303", "1ba02")
data = data.replace("1b304", "1ba03")
data = data.replace("1b305", "1ba04")
data = data.replace("1b307", "1ba06")
data = data.replace("1b308", "1ba07")

data = data.replace("1b311", "1ba08")
data = data.replace("1b312", "1ba09")
data = data.replace("1b313", "1ba0a")
data = data.replace("1b314", "1ba0b")
data = data.replace("1b315", "1ba0c")
data = data.replace("1b317", "1ba0e")
data = data.replace("1b318", "1ba0f")

data = data.replace("1b31e", "0323")
data = data.replace("1b31f", "0305")

with open(fn, 'w+') as f:
    f.write(data)
