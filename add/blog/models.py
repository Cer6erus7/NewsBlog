from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.title}'
