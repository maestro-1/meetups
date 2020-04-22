import unittest
from flask_script import Manager
from meetups import app

manager = Manager(app)


@manager.command
def tests():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
