from django.db import models
import os

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Create your models here.
def update_filename(instance, filename):
	ext = filename.split('.')[-1]
	tes = PostModel.objects.filter(author=instance.author)
	print(len(tes))
	id = PostModel.objects.latest('id')
	filename = "%s_%s.%s" % (instance.author.username, str(id.id+1), ext)
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

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if not self.slug:
			self.slug = slugify(f"{self.author.username} - {self.id}")
			self.save()

@receiver(post_delete, sender=PostModel)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False)