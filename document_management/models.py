from django.db import models
import uuid

class Document(models.Model):
    name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/')
    file_extension = models.CharField(max_length=10, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if self.file:
            self.file_extension = self.file.name.split('.')[-1].lower()
        super().save(*args, **kwargs)

