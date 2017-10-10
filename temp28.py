class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=' ')

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t=[]
t.append(Teacher('촘스키', 40, 31000))
t.append(Teacher('펌킨', 44, 38000))
t.append(Teacher('세이버', 41, 32000))
t.append(Teacher('맥과이어', 54, 35000))

s=[]
s.append(Student('싸이', 25, 65))
s.append(Student('홍길동', 26, 70))
s.append(Student('타디스', 29, 85))

print()
members = t + s
for member in members:
    member.tell()
