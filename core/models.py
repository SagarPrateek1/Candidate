from django.db import models

# Create your models here.
import datetime as dt
from mongoengine import Document, fields


class Candidate(Document):
    id = fields.IntField(primary_key=True)
    name = fields.StringField(max_length=100, required=True)
    contact_number = fields.StringField()
    email = fields.StringField()
    job_expectations = fields.DictField()
    work_details = fields.DictField()
    employment = fields.DictField()
    skills = fields.DictField()
    projects = fields.DictField()
    created = fields.DateTimeField()
