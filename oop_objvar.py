class Robot:
    """A robot with a name."""
    population = 0

    def __init__(self, name):
        """initialize data."""
        self.name = name
        print "(Initializing {})".format(self.name)

        # When some robot is created, the Robot will increase the population.
        Robot.population += 1

    def die(self):
        """I die"""
        print "{} is being destroyed!".format(self.name)

        Robot.population -= 1

        if Robot.population == 0:
            print "{} was the last one".format(self.name)
        else:
            print "There are still {:d} robots working.".format(Robot.population)

    def say_hi(self):
        """Sincere greetings from robots: You can do it."""
        print "Greeting, my masters call me {}.".format(self.name)

    @classmethod
    def how_many(cls):
        """print the current population"""
        print "We have {:d} robots.".format(cls.population)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print "\nRobots can do some work here.\n"

print "Robots have finished their work. So let's destroy them."
droid1.die()
droid2.die()

Robot.how_many()