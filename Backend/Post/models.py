from django.db import models
import os

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Create your models here.
def update_filename(instance, filename):
	ext = filename.split('.')[-1]
	try:
		post = PostModel.objects.filter(author=instance.author)
		id = len(post) + 1
	except Exception as e:
		id = 1
	filename = "%s_%s.%s" % (instance.author.username, str(id), ext)
	return filename

def upload_location(instance, filename, **kwargs):
	path = update_filename(instance, filename)
	file_path = 'posting/{username}/{img}'.format(username=str(instance.author.username), img=path)
	return file_path


class PostModel(models.Model):
	caption			= models.TextField(max_length=5000, null=False, blank=True)
	image			= models.ImageField(upload_to=upload_location, null=False, blank=True)
	date_published	= models.DateTimeField(auto_now_add=True, verbose_name='date published')
	date_updated	= models.DateTimeField(auto_now=True, verbose_name='date updated')
	author			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug 			= models.SlugField(blank=True, unique=True)

	def __str__(self):
		return self.slug

@receiver(post_delete, sender=PostModel)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False)

@receiver(pre_save, sender=PostModel)
def slug_save(sender, instance, **kwargs):
	if not instance.slug:
		try:
			len_user = PostModel.objects.filter(author=instance.author)
			count = len(len_user) + 1	
		except Exception as e:
			count = 1
		instance.slug = slugify(f"{instance.author.username} - {count}")
	else:
		img = sender.objects.get(slug=instance.slug)
		img.delete(False)