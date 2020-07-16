from django import forms

from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(max_length=120,
                           widget=forms.Textarea(
                               attrs={
                                   "type": "text",
                                   "placeholder": "Name",
                                    "class":"form-control",
                                   "id":"inputName"
                               }
                           ))
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder":"Comment",
            "id": "comment",
            "class":"form-control"
    }))


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'