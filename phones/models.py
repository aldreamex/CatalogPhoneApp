from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, verbose_name='Модель')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Изображение')
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=5, verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=300, verbose_name='URL')

    def __str__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exists}, {self.slug}'
