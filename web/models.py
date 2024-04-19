from django.db import models
import uuid #id unico
from django.utils.text import slugify 

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)#linea de texto
    description = models.TextField()#caja de texto
    image_url = models.URLField()
    slug = models.SlugField(unique=True, blank=True)#url amigable
    is_private = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)#polimorfismo, sobreescribe a models

    def __str__(self):
        return self.name
    
    #creo un modelo contact form

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.costumer_name


