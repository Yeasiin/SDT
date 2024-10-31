from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label="Enter Your Name")
    email = forms.EmailField(label="Enter Your Email")
    
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),label='About Your Self',help_text="Tell us about your self")
    date = forms.DateField(widget=forms.widgets.NumberInput({'type':'date'}),label="Date of Birth")
    
    gender = forms.ChoiceField(choices=[('male','Male'),('female','Female'),('others','Others')],label="Select Your Gender")
    
    course = forms.ChoiceField(widget=forms.RadioSelect, choices=[('database','Database'),('python','Python'),('sdt','SDT')],label="Current Course")
    
    
    
    
    
    
    check = forms.BooleanField(label="Agree to Terms & Conditions")
    
    