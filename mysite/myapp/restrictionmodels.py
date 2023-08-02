from django.db import models
from myapp.disbursementmodels import *

class ViewList(models.Model):
    id = models.BigIntegerField(primary_key=True)
    view_name = models.CharField(max_length=200,default=' ')
    

# Custom permissions for YourModel
class Meta:
    permissions = [
        ("can_do_something", "Can Do Something"),
        ("can_do_something_else", "Can Do Something Else"),
        ("can_manage_widgets", "Can Manage Widgets"),  # New permission
    ]