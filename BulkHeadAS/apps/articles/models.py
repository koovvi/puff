from django.db import models

class Flower(models.Model):
    name = models.CharField('Название цветка', max_length=255)
    price = models.DecimalField('Цена',max_digits=20, decimal_places=2, default=0.00)
    image = models.ImageField(blank=True, upload_to='img')
    description = models.TextField('Состав', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветки'

class Client(models.Model):
    client_name = models.CharField('ФИО', max_length=255)
    phone_number = models.CharField('Телефонный номер', max_length=255)
    client_adress = models.CharField('Адрес', max_length=255)
    client_flower = models.ForeignKey(Flower, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'