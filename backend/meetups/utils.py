import os
import secrets
from . import app, db
from fnmatch import fnmatch
from datetime import datetime
from meetups.models import Events


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
    return file_path


def date_store(date):
    date, time = date.strip().split(",")
    dt_cal = [int(x) for i, x in enumerate(date.split("-"))]
    dt_time = [int(x) for i, x in enumerate(time.split(":"))]
    year, month, day = dt_cal
    hour, minutes = dt_time
    date = datetime(year, month, day, hour, minutes)
    return date


async def datebase_entry(event, imageUrl):
    new_event = Events(title=event["title"], description=event["description"],
                       location=event["location"], date=event["date"],
                       imageUrl=imageUrl)
    db.session.add(new_event)
    db.session.commit()
