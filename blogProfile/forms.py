from django import forms
from blogPost.models import Blog_Users,Blog_Post
from django.utils import timezone

class Blog_edit_Form(forms.ModelForm):
	class Meta:
		model = Blog_Post
		fields = ['blog_title','blog_text','blog_image','date_publish']
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['blog_title'].widget.attrs.update({"class":"form-control","spellcheck":"false"})
		self.fields['blog_text'].widget.attrs.update({"class":"form-control","spellcheck":"false"})
		self.fields['date_publish'].widget.attrs.update({"class":"form-control"})
		self.fields['blog_image'].widget.attrs.update({"class":"form-control"})


class Blog_post_Form(forms.ModelForm):
	class Meta:
		model = Blog_Post
		fields = ['blog_title','blog_text','blog_image','date_publish']
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		nowTime = timezone.localtime()
		dateTime = nowTime.strftime("%Y-%m-%d %H:%M:%S")
		self.fields['blog_title'].widget.attrs.update({"class":"form-control","spellcheck":"false"})
		self.fields['blog_text'].widget.attrs.update({"class":"form-control","spellcheck":"false"})
		self.fields['date_publish'].widget.attrs.update({"class":"form-control",'value':dateTime,'placeholder':'YYYY-MM-DD h:m:s\t(24 hour format)','data-toggle':"tooltip",'data-placement':"bottom",'title':"24 Hours Format"})
		self.fields['blog_image'].widget.attrs.update({"class":"form-control",})
