from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

class Boyut(models.Model):
    boyut = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.boyut)

class Tip(models.Model):
    tip=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.tip)
class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)
    username = models.CharField(max_length=200,null=True)
    bio=models.TextField(null=True)
    phone_no=models.CharField(unique=True,null=True,max_length=11)
    avatar = models.ImageField(upload_to='images/',null=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

class Sehir(models.Model):
    sehir = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.sehir)

class Ilan(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200,verbose_name="Ilan adı")
    sehir = models.ForeignKey(Sehir,on_delete=models.SET_NULL, blank=True, null=True,)
    boyut = models.ForeignKey(Boyut,on_delete=models.SET_NULL, blank=True, null=True,)
    address = models.CharField(max_length=200)
    tip = models.ForeignKey(Tip,on_delete=models.SET_NULL, blank=True, null=True,)
    mahalle = models.CharField(max_length=200)
    metrekare=models.IntegerField(blank=True,null=True)
    sokak = models.CharField(max_length=200,null=True)
    yorumcular = models.ManyToManyField(
        User, related_name='yorumcular', blank=True)
    price = models.IntegerField(verbose_name="Fiyat")
    image = models.ImageField(upload_to = 'images/',null=True, blank = True)
    image1 = models.ImageField(upload_to = 'images/',null=True, blank = True)
    image2 = models.ImageField(upload_to = 'images/',null=True, blank = True)
    image3 = models.ImageField(upload_to = 'images/',null=True, blank = True)
    image4 = models.ImageField(upload_to = 'images/',null=True, blank = True)
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if self._state.adding:
            super().save(*args, **kwargs)
            Fiyat.objects.create(ilan_id=self.pk,eski_fiyat=self.price)
        elif not self._state.adding:
            Fiyat.objects.create(ilan_id=self.pk,eski_fiyat=self.price)
            super().save(*args, **kwargs)


class Yorum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE)
    text=models.TextField()
    tarih=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-tarih']

    def __str__(self):
        return self.text

class Kaydet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ilan.id)

class Fiyat(models.Model):
    ilan_id = models.CharField(max_length=200,blank=True,null=True)
    eski_fiyat = models.CharField(max_length=200,blank=True,null=True)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.eski_fiyat)