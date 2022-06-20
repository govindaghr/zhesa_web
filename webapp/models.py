from django.db import models
from .storage import OverwriteStorage


# Create your models here.
class PhelkayWord(models.Model):
    phelkay_word = models.CharField(max_length=255, unique=True)
    p_phrase = models.CharField(max_length=255, null=True, blank=True,)
    publish_date = models.DateTimeField(auto_now=True,editable=False)

    class Meta:
        ordering = ['phelkay_word']

    def __str__(self):
        return self.phelkay_word

class ZhebsaWord(models.Model):
    zhebsa_word = models.CharField(max_length=255, unique=True)
    z_phrase = models.CharField(max_length=255, null=True, blank=True,)
    audio = models.FileField(upload_to = 'zhesaAudio/', null=True, blank=True, storage=OverwriteStorage()) #replace file with OverwriteStorage() method
    publish_date = models.DateTimeField(auto_now=True,editable=False) #change to auto   auto_now_add=True, default=django.utils.timezone.now
    phelkay = models.ManyToManyField(PhelkayWord, related_name='zhesa') # search or able to do without drop down list.

    def Mapped_words(self):                 # View 
        return ",".join([str(p) for p in self.phelkay.all()])

    class Meta:
        ordering = ['zhebsa_word']

    def __str__(self):
        return self.zhebsa_word

""" class MapDzongkhaZhebsa(models.Model):
    map_id = ManyToManyField(ZhebsaWord) """

class ContactDetails(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    email= models.EmailField(max_length=70)
    contact_date = models.DateTimeField(auto_now_add=True,editable=False)
    comments= models.TextField()

    def __str__(self):
       return self.firstname