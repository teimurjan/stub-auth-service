import os
from flask_script import Manager

from app import create_app
from settings import BASE_DIR

app = create_app()
manager = Manager(app)


@manager.command
def runserver():
    app.run(debug=True, host='0.0.0.0', port=5000)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover(os.path.join(BASE_DIR, 'tests'))
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
