# 1
class Person:
    pass # An empty block

p = Person()
print(p)


# 2
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()


# 3
def sum_ab(a,b):
    print('a+b=', a+b)

sum_ab(1,2)

def say_hi():
    print('Hi !')

say_hi()


# 4
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Baram')
p.say_hi()


# 5
class Person:
    def __init__(self, name):
        self.n = name
    def say_hi(self):
        print('Hello, my name is', self.n)

p = Person('Storm')
p.say_hi()


# 6
class Robot:
    """Represents a robot, with a name."""
    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))
        # 객체(로봇)이 만들어지면 population 을 1 더합니다.
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))

        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot.
        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

#    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()

classmethod(Robot.how_many)    # 삭제
#Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
classmethod(Robot.how_many)    # 삭제
#Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished work. So let's destroy them.")

droid1.die()
droid2.die()
classmethod(Robot.how_many)    # 삭제
#Robot.how_many()
