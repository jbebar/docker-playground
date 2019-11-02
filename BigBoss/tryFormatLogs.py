from formatLogs import extractAddressFromRequest

#d = dict('firstLine','jell')
s = "Arsenal"
addr = "1.2"
#Create an iterable containing a tuple with just two values : the key and the value pair
kv1=[(addr,s)]
#Insert iterable into the dict
d = dict(kv1)
#See all the values in the dict
for val in d.values():
    print("Value : ", val)
#Get a value from dict associtated to a specific key
print("Value at " + addr + " key : " + d[addr])
#Create a an iterable containing an iterable with just two values : the key and the value pair.
kv2=[["1.3","Chelsea"]]
#Insert a new key in the dict
d.update(kv2)

for val in d.values():
    print("Value : ", val)

#Update a value
d.update([(addr,"Arsenal is my favourite team")])

print("Value at " + addr + " key : " + d[addr])

print(extractAddressFromRequest("|IPAdress|lastLaunched|version|lastAverageFrameRate|status|"))