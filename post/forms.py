from django import forms

from post.models import Post
visibility_choices = (
    (1,"Public"),
    (2,"Private"),
)
class PostForm(forms.ModelForm):
    visibility = forms.MultipleChoiceField(choices=visibility_choices)
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ["user","last_updated"]
