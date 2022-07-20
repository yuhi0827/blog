from tkinter import Label
from django import forms

class PostForm(forms.Form):
  title = forms.CharField(max_length=30, Label='タイトル')
  content = forms.CharField(Label='内容', widget=forms.Textarea())
  image = forms.ImageField(Label='イメージ画像',required=False)