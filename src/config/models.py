from django.db import models

# Create your models here.
class PageVisibilityConfig(models.Model):
    page = models.CharField(max_length=128, null=False, blank=False, unique=True)
    visible = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.page