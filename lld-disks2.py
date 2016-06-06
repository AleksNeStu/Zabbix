#!/usr/bin/python
import os
# import json
import simplejson
from decimal import Decimal


a = os.listdir("/sys/class/block")
try:
	a.remove("sr")
except ValueError:
	pass
try:
	a.remove("loop")
except ValueError:
	pass
try:
	a.remove("ram")
except ValueError:
	pass

# for x in a: print x
data = [{"{#DEVICENAME}": x} for x in a]
print(simplejson.dumps({"data": data}, indent=4))