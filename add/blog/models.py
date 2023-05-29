from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/')

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.title}'
