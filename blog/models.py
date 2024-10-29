from django.db import models


class Articles(models.Model):
    headline = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    pub_date = models.DateField()

    def __str__(self):
        return self.headline
