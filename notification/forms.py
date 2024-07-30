from django import forms
from .models import Notification
from users.forms import messages
from users.models import User


class CreateNotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields=['category', 'short_description', 'content', 'link']
        widgets = {
            'category': forms.Select(),
            'short_description':forms.TextInput(),
            'content': forms.Textarea(attrs={
                'class': 'text-end p-1 m-1', 
                "placeholder": "محتوای پیام"
            }),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'category': "موضوع",
            'short_description' : 'توضیح کوتاه',
            'content' : 'محتوا',
            'link' : 'لینک',
        }
        error_messages = messages

    def __init__(self, *args, **kwargs):
        super(CreateNotificationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = visible.field.widget.attrs.get('class', '') + "text-end form-control"