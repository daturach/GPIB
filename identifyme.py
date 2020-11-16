import time
import gpib

mydevice = gpib.find("pm6666")  # defined in /etc/gpib.conf in the device section

def query(handle, command, numbytes=100):
    gpib.write(handle, command)
    time.sleep(0.1)
    response = gpib.read(handle, numbytes)
    return response

print (query(mydevice, "ID?"))  # identification command for your equipment
gpib.close(mydevice)

