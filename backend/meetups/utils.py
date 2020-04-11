import os
import secrets
from PIL import Image
from . import app, db, bcrypt
from fnmatch import fnmatch
from meetups.appy import client
from datetime import datetime
from meetups.models import Events, Users


def uploads(file, path):
    if not (fnmatch(file.filename, "*.jpeg") or
            fnmatch(file.filename, "*.png") or
            fnmatch(file.filename, "*.jpg")):
        return "Not an image"

    fname = secrets.token_hex(10)
    _, fext = os.path.splitext(file.filename)
    final_name = fname + fext
    file_path = os.path.join(app.static_folder, path, final_name)
    file.save(file_path, buffer_size=16384)
    file.close()
    i = Image.open(file_path)
    i.thumbnail((1000, 562))
    i.save(file_path)
    return file_path


def date_store(date):
    date, time = date.strip().split(",")
    dt_cal = [int(x) for i, x in enumerate(date.split("-"))]
    dt_time = [int(x) for i, x in enumerate(time.split(":"))]
    year, month, day = dt_cal
    hour, minutes = dt_time
    date = datetime(year, month, day, hour, minutes)
    return date


# @client.task
def event_entry(event, imageUrl):
    new_event = Events(title=event["title"], description=event["description"],
                       location=event["location"], date=event["date"],
                       imageUrl=imageUrl)
    db.session.add(new_event)
    db.session.commit()


# @client.task
def user_entry(user):
    password = bcrypt.generate_password_hash(user["password"].strip()).decode('utf-8')
    new_event = Users(full_name=user["full_name"], contact=user["contact"],
                      email=user["email"], password=password)
    db.session.add(new_event)
    db.session.commit()
