def two_sort(strings):
    strings.sort()
    first = strings[0]
    return '***'.join(first)

class Person:
    def __init__(self, first_name, last_name, father_name):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name

    def __str__(self):
        return f"{self.first_name} {self.father_name} {self.last_name}"