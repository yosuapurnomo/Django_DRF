from rest_framework import serializers

from Post.models import PostModel

class PostSerializers(serializers.ModelSerializer):

	username = serializers.SerializerMethodField('get_username_from_author')

	class Meta:
		model = PostModel
		fields = ['caption', 'image', 'date_published', 'date_updated', 'slug', 'username']


	def get_username_from_author(self, model):
		username = model.author.username
		print(username)
		return username