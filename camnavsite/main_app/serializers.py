# from rest_framework import serializers
from .models import Category, Article, Photo, Newsletter

# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class FileListSerializer (serializers.Serializer) :
#     image = serializers.ListField(
#                        child=serializers.FileField( max_length=100000,
#                                          allow_empty_file=False,
#                                          use_url=False )
#                                 )
#     def create(self, validated_data):
#         blogs=Article.objects.latest('created_at')
#         image=validated_data.pop('image')
#         for img in image:
#             photo=Photo.objects.create(image=img,blogs=blogs,**validated_data)
#         return photo
#
#
# class PhotoSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Photo
#         fields = '__all__'
#         # read_only_fields = ("articles",)
#
#
# class NewsletterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Newsletter
#         fields = '__all__'
