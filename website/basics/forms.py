from django import forms


class InterestForm(forms.Form):
    amount = forms.FloatField(label='Amount')
    rate = forms.FloatField(label='Interest Rate', min_value = 5, max_value = 50)


class AuthorForm(forms.Form):
    fullname = forms.CharField(label="Fullname")
    email = forms.EmailField(label="Email")
    mobile = forms.RegexField(label="Mobile", regex=r"\d+")

