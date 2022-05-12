
from datetime import datetime
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _
import random
import string
from django.core.validators import validate_email
import re

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATE_TIME_FORMAT = "{0} {1}".format(DATE_FORMAT, TIME_FORMAT)

PHONE_PAT = re.compile('^1[3|5|7|8|][0-9]{9}$')


def isDateFormat(date, format="datetime"):

    if date is None:
        return date

    if format == "datetime":
        try:
            date_time = datetime.strptime(date, DATE_TIME_FORMAT)
        except:
            raise ValidationError(_("DateTime Format error."))
    else:
        try:
            date_time = datetime.strptime(date, DATE_FORMAT)
        except:
            raise ValidationError(_("Date Format error."))

    return date_time


def str2bool(v):
    if isinstance(v, bool):
        return v

    return str(v).lower() in ("yes", "true", "t", "1")


def generateCode(num=6):
    code = ''.join(random.sample(string.ascii_letters + string.digits, num))
    return code


def validEmail(email):
    try:
        validate_email(email)
    except:
        return False
    return True


def validPhone(phone):
    if not phone:
        return False

    match = PHONE_PAT.match(phone)
    return match is not None

