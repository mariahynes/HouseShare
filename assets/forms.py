from django import forms

class InviteCodeForm(forms.Form):
    invitecode = forms.CharField(max_length=5, label="Your Invite Code")

