from django import forms



class ContactForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
                "class":"form-control",
                "rows":"6",
                "id":"input-text-area",
                "name":"text",
                "placeholder":"ادخل النص هنا",
                "onkeyup" : "checkInputText(this)"
            }), label="", max_length=500)
    

class SoundForm(forms.Form):
    soundfile = forms.FileField(
        label='حمل ملفاً صوتياً',
        help_text='الحد الأقصى 10  ميجابايت'
    )
    

