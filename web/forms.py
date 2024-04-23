from django import forms
from .models import ContactForm
from .models import Comment

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email','customer_name','message']
        labels = {
                    'customer_email': 'Correo electronico',
                    'customer_name' : 'Nombre',
                    'message': 'Mensaje'}
        



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] 