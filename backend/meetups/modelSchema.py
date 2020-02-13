import re
from .utils import date_store
from marshmallow import (Schema, fields, post_load, pre_load, post_dump,
                         validate, validates, ValidationError)


class UserSchema(Schema):
    full_name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    contact = fields.Integer(required=True)
    email = fields.Email(required=True, validate=validate.Email())
    imageUrl = fields.Str(dump_only=True)

    @pre_load
    def sanitize(self, data, **kwargs):
        data["full_name"] = data["full_name"].strip()
        data["contact"] = data["contact"].strip()
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


class LoginSchema(Schema):
    password = fields.Str(required=True, load_only=True)
    email = fields.Email(required=True, validate=validate.Email())

    @pre_load
    def sanitize(self, data, **kwargs):
        data["password"] = data["password"].strip()
        data["email"] = data["email"].strip()
        return data


class EventSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    date = fields.Str(required=True)
    imageUrl = fields.Str(dump_only=True)

    @pre_load
    def sanitize(self, data, **kwargs):
        data["title"] = data["title"].strip()
        data["description"] = data["description"].strip()
        data["location"] = data["location"].strip()
        return data

    @post_load
    def dateIssues(self, data, **kwargs):
        data["date"] = date_store(data["date"])
        return data

    @post_dump
    def imaging(self, data, **kwargs):
        data["imageUrl"] = data["imageUrl"].split("/")[-1]
        return data
