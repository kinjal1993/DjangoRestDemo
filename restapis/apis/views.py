from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.settings import import_from_string
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status
from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id = None):
        return self.update(request,id)

    def delete(self,request,id = None):
        return self.destroy(request,id)

class ArticleAPIView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArticleSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)

        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):

    def get_object(self,id):
        try:
            article = Article.objects.get(id=id)
            return article

        except Article.DoesNotExist:
            return Response(status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)

        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def article_list(request):

#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many = True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = ArticleSerializer(request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status.HTTP_200_OK)

#         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def article_detail(request,pk):

#     try:
#         article = Article.objects.get(id=pk)

#     except Article.DoesNotExist:
#         return Response(status.HTTP_400_BAD_REQUEST)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article,data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status.HTTP_200_OK)

#         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)