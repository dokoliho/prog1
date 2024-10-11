

r = 1

def get_random():
    global r
    r = (r * 123456789 + 987654321) % 1000000003
    return r

print(get_random())
print(get_random())
