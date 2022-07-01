from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorycar', null=True)
    name = models.CharField('Car name', max_length=30)
    price = models.IntegerField('Car price')
    about = models.TextField('Car about')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
