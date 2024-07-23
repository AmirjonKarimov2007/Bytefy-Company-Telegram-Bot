from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name



class Service(models.Model):
    fullname = models.CharField(verbose_name='Xizmat nomi', max_length=100)
    photo = models.CharField(verbose_name="Rasm", max_length=300)
    description = models.TextField(verbose_name="Xizmat haqida", max_length=3000)

    def __str__(self):
        return f"{self.fullname}"
class Arizalar(models.Model):
    id = models.AutoField(verbose_name='Ariza Raqami', primary_key=True)
    name = models.CharField(verbose_name="Ism Familiya", max_length=100)
    username = models.CharField(verbose_name='Username', max_length=100, null=True, blank=True)
    user_id = models.BigIntegerField(verbose_name='Telegram_id')
    phone_number = models.CharField(verbose_name='Telefon raqami', max_length=15, null=True, blank=True)

    # Yangi field service
    service = models.ForeignKey(Service, verbose_name='Xizmat', on_delete=models.SET_NULL, null=True, blank=True)
    selected_package = models.CharField(verbose_name='Tanlangan Paket', max_length=20, choices=[('Basic', 'Basic'), ('Standard', 'Standard'), ('Premium', 'Premium')], null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user_id})"
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
