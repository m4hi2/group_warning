from django.db import models


class WarnedUser(models.Model):
    # Facebook username or profile id of the warned user
    user_id = models.CharField(max_length=50)
    warning_count = models.IntegerField(default=1)
