import sys
import time
import Gpib
#inst = Gpib.Gpib(0,6)
inst = Gpib.Gpib("pm6666")

inst.write("ID?")
time.sleep(0.1)
resp = inst.read(100)
time.sleep(0.1)
print (resp)
inst.close()

