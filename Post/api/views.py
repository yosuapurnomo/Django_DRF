from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Post.models import PostModel
from Account.models import Account
from .serializers import PostSerializers

@api_view(['GET',])
def api_detail_view(request, slug):
	data = {}
	try:
		post_model = PostModel.objects.get(slug=slug)
		data['success'] = 'Data ditemukan'
	except PostModel.DoesNotExist:
		data['failure'] = 'Data tidak ditemukan'
		return Response(data=data, status=status.HTTP_404_NOT_FOUND, )

	if request.method == 'GET':
		serializer = PostSerializers(post_model)
		return Response(serializer.data)

@api_view(['PUT', ])
def api_update_view(request, slug):
	try:
		post_model = PostModel.objects.get(slug=slug)
	except PostModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = PostSerializers(post_model, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['success'] = "Update success"
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['DELETE'],)
def api_delete_view(request, slug):
	try:
		post_model = PostModel.objects.get(slug=slug)
	except PostModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'DELETE':
		operations = post_model.delete()
		data = {}
		if operations:
			data['success'] = 'delete success'
		else:
			data['failure'] = 'delete failed'
		return Response(data=data)

@api_view(['POST'],)
def api_create_view(request):
	account = Account.objects.get(pk=1)
	print(account)
	if request.method == 'POST':
		post_model = PostModel(author=account)
		serializer = PostSerializers(post_model, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, staus=status.HTTP_404_BAD_REQUEST)

