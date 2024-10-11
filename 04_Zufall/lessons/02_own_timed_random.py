from time import time

# time() gibt die aktuelle Zeit in Sekunden seit dem 1.1.1970 zurück
r = int(time())

def get_random():
    global r
    r = (r * 123456789 + 987654321) % 1000000003
    return r

print(get_random())
print(get_random())