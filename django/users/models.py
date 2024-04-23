from django.db import models

class User(models.Model):
    name = models.CharField(verbose_name='Fullname', max_length=100)
    username = models.CharField(verbose_name='Username', max_length=100, null=True)
    user_id = models.BigIntegerField(verbose_name='Telegram_id', unique=True)

    def __str__(self):
        return self.name



class Services(models.Model):
    name = models.CharField(verbose_name='Fullname', max_length=100)
    photo = models.CharField(verbose_name="Rasm", max_length=200)
    description = models.TextField(verbose_name="Xizmat haqida")
    
    BASIC = 'Basic'
    STANDARD = 'Standard'
    PREMIUM = 'Premium'
    
    basic_price = models.DecimalField(verbose_name="Basic package price", decimal_places=2, max_digits=8, null=False)
    standard_price = models.DecimalField(verbose_name="Standard package price", decimal_places=2, max_digits=8, null=False)
    premium_price = models.DecimalField(verbose_name="Premium package price", decimal_places=2, max_digits=8, null=False)
    
    def __str__(self):
        return f"{self.name}"
