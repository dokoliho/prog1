# Typen und ihre Konvertierung
def typfehler():
    p = '10'
    for _ in range(p):
        print('no way!')

print(int("10"))
#print(int("10.6"))
#print(int("A"))
print(int(10.0))
print(int(10.3))
print(int(10.7))

print(str(10.7))

print(float(10))
print(float("10"))
print(float("10.7"))
#print(float("A"))

#  Range erwartet Ganzzahlen
p = '10'
for _ in range(int(p)):
    print('way!')

# Ganzzahlige Division // vs Gleitkomma-Division /
print(3 // 2)
print(3 / 2)

# Boolescher Typ
t = True
print(type(t))
