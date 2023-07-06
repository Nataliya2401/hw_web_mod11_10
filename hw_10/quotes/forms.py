from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField, \
    CharField, Textarea, TextInput, Select, SelectMultiple, DateTimeField, BooleanField
from .models import *


class AddAuthorForm(ModelForm):
    fullname = CharField(max_length=128, label="Full name", widget=TextInput(attrs={"class": "form-control"}))
    born_date = CharField(max_length=40, label="Date of burn", widget=TextInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=128, required=False, label="Place of burn", widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(label="About", required=False, widget=Textarea(attrs={'cols': 140, 'rows': 15}))
    # is_published = BooleanField()

    class Meta:
        model = Author
        fields = ("fullname", "born_date", "born_location", "description", )


class AddQuoteForm(ModelForm):
    quote = CharField(widget=Textarea(attrs={'cols': 160, 'rows': 15}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by("fullname"),
                              required=False, label="Author", empty_label="No Author", widget=Select())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by("name"), required=False, widget=SelectMultiple())

    class Meta:
        model = Quote
        fields = ("quote", "author", "tags",)

