from django import forms
from .models import ForumSectionModel , CommentModel

class NewTopicForm(forms.ModelForm):

    massg = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5,'placeholder':'What is on your mind?'}
    ),
    max_length=4000,
    help_text='The max length of the text is 4000')

    class Meta:
        model = ForumSectionModel
        fields = ['SectionSubject','massg']


class PostForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['massg',]