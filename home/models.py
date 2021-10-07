from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    age = models.PositiveIntegerField(verbose_name='Возраст', default=0)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='actors/', verbose_name='изображение')
    text = models.TextField(blank=True, verbose_name='достижение')
    email = models.EmailField(verbose_name='почта')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агент'

