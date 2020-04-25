import re
from flask import url_for
from .utils import date_store
from marshmallow import (Schema, fields, post_load, pre_load, post_dump,
                         validate, validates, ValidationError)


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
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
        pattern = re.compile(r"[\W+]")
        num = re.compile(r"\d+")

        if (not pattern.search(data) or
                not num.findall(data) or
                len(data) < 8 or len(data) > 15):
            raise ValidationError('Password must contain at least 8 characters, one numeric, one special and one Uppercase')


class LoginSchema(Schema):
    password = fields.Str(required=True, load_only=True)
    email = fields.Email(required=True, validate=validate.Email())

    @pre_load
    def sanitize(self, data, **kwargs):
        data["password"] = data["password"].strip()
        data["email"] = data["email"].strip()
        return data


class UpdateUserSchema(Schema):
    id = fields.Integer(dump_only=True)
    full_name = fields.Str()
    contact = fields.Integer()
    email = fields.Email(validate=validate.Email())


class EventSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    location = fields.Str(required=True)
    date = fields.Str(required=True)
    imageUrl = fields.Str(dump_only=True)
    guest = fields.Nested('UpdateUserSchema', many=True)

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
        data["imageUrl"] = url_for('static', filename='event_image/' +
                                   data["imageUrl"].split("/")[-1])
        return data
