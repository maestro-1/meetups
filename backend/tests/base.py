from flask_testing import TestCase
from meetups import app, db, bcrypt
from meetups.config import TestConfig
from meetups.models import Events, Users, Guests
from datetime import date


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        return app

    @classmethod
    def setUp(cls):
        # create database
        db.create_all()

        # insert test data into database

        # host passwords
        pass1 = bcrypt.generate_password_hash('Smaug'.strip()).decode('utf-8')
        pass2 = bcrypt.generate_password_hash('Ariana'.strip()).decode('utf-8')

        # add test users
        db.session.add(Users(full_name='Anino Ifediora', password=pass2,
                             contact='090549812758', email='anino@gmail.com'))
        db.session.add(Users(full_name='Osakwe Chuwkuka', password=pass1,
                             contact='070457248571', email='chuwk32@gmail.com'))

        # add test events
        db.session.add(Events(title='maestro expo', description='Tech conference for robotics innovation',
                              location='Delta, Nigeria', date=date(2020, 3, 28)))
        db.session.add(Events(title='Heart Enlargement', description='The gospel enlarging your heart',
                              location='Ibadan, Nigeria', date=date(2020, 3, 28)))

        # add test guests
        db.session.add(Guests(full_name='David Benz', contact='07021954837',
                              email='Benz@gmail.com'))
        db.session.add(Guests(full_name='Jane Doe', contact='09014598632',
                              email='Doe@yahoo.com'))

        # persist database entry
        db.session.commit()

        # Host relationship
        host1 = Users.query.get(1)
        host2 = Users.query.get(2)

        event1 = Events.query.get(1)
        event2 = Events.query.get(2)

        host1.event.append(event1)
        host2.event.append(event1)
        host1.event.append(event2)

        # Guest relationship
        guest1 = Guests.query.get(1)
        guest2 = Guests.query.get(2)

        event1 = Events.query.get(1)
        event2 = Events.query.get(2)

        event1.guest.append(guest1)
        event2.guest.append(guest2)
        event1.guest.append(guest2)

        db.session.commit()

    @classmethod
    def tearDown(cls):

        # delete all in database
        db.session.remove()

        # destroy datbase
        db.drop_all()
