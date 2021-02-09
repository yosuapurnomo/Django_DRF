from django.db import models

from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Create your models here.
def upload_location(instance, filename, **kwargs):
	file_path = 'posting/{username}/{img}'.format(username=str(instance.author.username), img=filename)
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

def pre_save_posting(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-" + instance.id)

pre_save.connect(pre_save_posting, sender=PostModel)