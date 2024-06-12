from django.db import models

class User(models.Model):
    name = models.CharField(verbose_name='Fullname', max_length=100)
    username = models.CharField(verbose_name='Username', max_length=100, null=True)
    user_id = models.BigIntegerField(verbose_name='Telegram_id', unique=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    fullname = models.CharField(verbose_name='Xizmat nomi', max_length=100)
    photo = models.CharField(verbose_name="Rasm", max_length=300)
    description = models.TextField(verbose_name="Xizmat haqida", max_length=3000)

    def __str__(self):
        return f"{self.fullname}"

class BasicService(models.Model):
    iid = models.IntegerField(default=1, editable=False, verbose_name='ID')
    fullname = models.CharField(max_length=255, default="Basic", editable=False, verbose_name='Full Name')
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='basic_service', null=True, blank=True)
    description = models.TextField(verbose_name="Xizmat haqida - Basic")
    price = models.DecimalField(verbose_name="Basic package price", decimal_places=2, max_digits=15)

    def __str__(self):
        return f"Basic Service: {self.description[:50]}"

class StandardService(models.Model):
    iid = models.IntegerField(default=2, editable=False, verbose_name='ID')
    fullname = models.CharField(max_length=255, default="Standard", editable=False, verbose_name='Full Name')
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='standard_service', null=True, blank=True)
    description = models.TextField(verbose_name="Xizmat haqida - Standard")
    price = models.DecimalField(verbose_name="Standard package price", decimal_places=2, max_digits=15)

    def __str__(self):
        return f"Standard Service: {self.description[:50]}"

class PremiumService(models.Model):
    iid = models.IntegerField(default=3, editable=False, verbose_name='ID')
    fullname = models.CharField(max_length=255, default="Premium", editable=False, verbose_name='Full Name')
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='premium_service', null=True, blank=True)
    description = models.TextField(verbose_name="Xizmat haqida - Premium")
    price = models.DecimalField(verbose_name="Premium package price", decimal_places=2, max_digits=15)

    def __str__(self):
        return f"Premium Service: {self.description[:50]}"
