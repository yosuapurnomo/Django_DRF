from rest_framework import serializers

from Post.models import PostModel

class PostSerializers(serializers.ModelSerializer):
	class Meta:
		model = PostModel
		fields = ['caption', 'image', 'date_published', 'date_updated', 'slug']