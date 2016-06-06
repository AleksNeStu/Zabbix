#!/usr/bin/python
import os

if os.path.exists("/sys/class/block"):
	a = list(os.listdir("/sys/class/block"))
if os.path.exists("/sys/block"):
	a = list(os.listdir("/sys/block"))
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
# data = [{"{#DEVICENAME}": x} for x in a]
# print(simplejson.dumps({"data": data}, indent=4))
print """{
    "data": ["""
for i in range(0,len(a)-1):
	print "        {"
	print """            "{#DEVICENAME}": """ + '"' + a[i] + '"'
	print "        },"

print "        {"
print """            "{#DEVICENAME}": """ + '"' + a[len(a)-1] + '"'
print "        }"

print """    ]
}"""