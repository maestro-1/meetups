import os
import re
import secrets
from fnmatch import fnmatch
from . import bcrypt, app
from PIL import Image
from marshmallow import (Schema, fields, post_load, pre_load,
                         validate, validates, ValidationError)


def uploads(file, path):
    if not fnmatch("*.jpeg") or fnmatch("*.png"):
        return

    fname = secrets.token_hex(10)
    _, fext = os.path.splitext(file)
    final_name = fname + fext
    file_path = os.path.join(app.static_folder, path, final_name)
    i = Image.open(file)
    i.save(file_path)
    return final_name


class UserSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    contact = fields.Integer(required=True)
    email = fields.Email(required=True, validate=validate.Email())
    imageUrl = fields.Str()

    @post_load
    def adjust_data(self, data, **kwargs):
        data["password"] = bcrypt.generate_password_hash(data["password"].strip())
        data["imageUrl"] = uploads(data["imageUrl"], "profile_image")
        return data

    @pre_load
    def sanitize(self, data, **kwargs):
        data["first_name"] = data["first_name"].strip()
        data["last_name"] = data["last_name"].strip()
        data["Address"] = data["Address"].strip()
        data["email"] = data["email"].strip()
        return data

    @validates("password")
    def strength(self, data):

        pattern = re.compile(r"(([\W+_])([A-Z]))")
        num = re.compile(r"\d+")

        try:
            if not pattern.search(data).group(2) and pattern.search(data).group(3):
                raise ValidationError("""
                        Password must contain at least 8 characters, one numeric, one special and one Uppercase
                     """)
            elif not num.findall(data):
                raise ValidationError("""
                        Password must contain at least 8 characters, one numeric, one special and one Uppercase
                     """)
            elif len(data) < 8 or len(data) > 15:
                raise ValidationError("Password cannot be less than 8 characters")
        except Exception:
            raise ValidationError("""
                        Password must contain at least 8 characters one numeric, one special and one Uppercase
                     """)


class EventSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    date = fields.Str(required=True)
    imageUrl = fields.Str(required=True)

    @pre_load
    def sanitize(self, data, **kwargs):
        data["name"] = data["name"].strip()
        data["description"] = data["description"].strip()
        data["location"] = data["location"].strip()
        data["date"] = data["date"].strip()
        data["imageUrl"] = data["imageUrl"]
        return data

    @post_load
    def file_lock(self, data, **kwargs):
        data["imageUrl"] = uploads(data["imageUrl"], "event_image")
        return data
