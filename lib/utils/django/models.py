# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.fields import BigAutoField

class AutoFieldUnsigned(models.AutoField):

    def __init__(self, *args, **kwargs):
        super(AutoFieldUnsigned, self).__init__(*args, **kwargs)

    def db_type(self,connection):
        return "int UNSIGNED AUTO_INCREMENT"


class BigAutoFieldUnsigned(BigAutoField):

    def __init__(self, *args, **kwargs):
        super(BigAutoFieldUnsigned, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return "bigint UNSIGNED AUTO_INCREMENT"


