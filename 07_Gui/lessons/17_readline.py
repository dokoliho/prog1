def do_something_with_line(line):
    print(line, end="")

with open("particle.py", "r") as f:
    line = f.readline()
    while len(line)>0:
        do_something_with_line(line)
        line = f.readline()

