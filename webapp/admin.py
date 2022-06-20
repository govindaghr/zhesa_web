from django.contrib import admin
from .models import ZhebsaWord, PhelkayWord, ContactDetails
# Register your models here.
@admin.register(PhelkayWord)
class PhelkayWordAdmin(admin.ModelAdmin):
    list_display = ['phelkay_word', 'p_phrase', 'publish_date']
@admin.register(ZhebsaWord)
class ZhebsaWordAdmin(admin.ModelAdmin):
    list_display = ['zhebsa_word', 'z_phrase', 'publish_date', 'Mapped_words']

@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'comments']
