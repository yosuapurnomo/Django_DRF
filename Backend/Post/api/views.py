from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

from Post.models import PostModel
from Account.models import Account
from .serializers import PostSerializers

@api_view(['GET',])
# @permission_classes((IsAuthenticated, ))
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
@permission_classes((IsAuthenticated, ))
def api_update_view(request, slug):
	try:
		post_model = PostModel.objects.get(slug=slug)
	except PostModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if post_model.author != user:
		return Response({'response': "You dont have permission to edit that"})

	if request.method == 'PUT':
		serializer = PostSerializers(post_model, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['success'] = "Update success"
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['DELETE'],)
@permission_classes((IsAuthenticated, ))
def api_delete_view(request, slug):
	try:
		post_model = PostModel.objects.get(slug=slug)
	except PostModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if post_model.author != user:
		return Response({'response': "You dont have permission to edit that"})

	if request.method == 'DELETE':
		operations = post_model.delete()
		data = {}
		if operations:
			data['success'] = 'delete success'
		else:
			data['failure'] = 'delete failed'
		return Response(data=data)

@api_view(['POST'],)
@permission_classes((IsAuthenticated, ))
def api_create_view(request):
	account = request.user
	if request.method == 'POST':
		post_model = PostModel(author=account)
		serializer = PostSerializers(post_model, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, staus=status.HTTP_404_BAD_REQUEST)

@api_view(['GET'])
def api_list_post(request):
	if request.method == 'GET':
		post_model = PostModel.objects.all()
		serializer = PostSerializers(post_model, many=True)
		# print(post_model)
		return Response(serializer.data)

class listPost(ListAPIView):
	queryset = PostModel.objects.all()
	serializer_class = PostSerializers
	authentication_class = (None)
	permission_class = (None)
	pagination_class = PageNumberPagination
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('caption', 'author')

class createPost(CreateAPIView):
	serializer_class = PostSerializers
	authentication_class = (TokenAuthentication)
	permission_class = (IsAuthenticated)

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

	def get_success_headers(self, data):
		try:
			return {
			'success':"Create success"
			}
		except (TypeError, KeyError):
			return {
			'failed':"Create failed"
			}

class updatePost(UpdateAPIView):
	queryset = PostModel.objects.all()
	serializer_class = PostSerializers
	authentication_class = (TokenAuthentication)
	permission_class = (IsAuthenticated)
	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'

	def put(self, request, *args, **kwargs):
		obj = self.get_object()
		print(obj)

		if obj.author != request.user:
			return Response({'response': "You dont have permission to edit that"})
		return self.update(request, *args, **kwargs)

class detailPost(RetrieveAPIView):
	queryset = PostModel.objects.all()
	serializer_class = PostSerializers
	authentication_class = (TokenAuthentication)
	permission_class = (IsAuthenticated)
	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'

class deletePost(DestroyAPIView):
	queryset = PostModel.objects.all()
	serializer_class  = PostSerializers
	authentication_class = (TokenAuthentication)
	permission_class = (IsAuthenticated)
	lookup_field = 'slug'
	lookup_url_kwarg = 'slug'

	def destroy(self, request, *args, **kwargs):
		user = self.get_object()
		if user.author != request.user:

			return Response({'failure': "You dont have permission to delete that"})

		self.perform_destroy(user)
		return Response({'success': "Delete success"}, status=status.HTTP_204_NO_CONTENT)