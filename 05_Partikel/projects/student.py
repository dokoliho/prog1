class Student:
    def __init__(self, name, matrikelnummer):
        self._name = name
        self._matrikelnummer = matrikelnummer

    def __str__(self):
        return f"Student (Name: {self._name}, Matrikelnummer: {self._matrikelnummer})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self._matrikelnummer == other._matrikelnummer
        else:
            return False

s = Student("Max", 123456)
print(s)

s1 = Student("Erika", 654321)
s2 = Student("Erika", 654321)

print(s1 == s2)
print(id(s1) == id(s2))