from rest_framework import serializers
from .models import Article, User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body']
        # depth = 1


class ArticleSerializerAnonymous(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary', 'firstParagraph']
        # depth = 1

class ArticleSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'category', 'title', 'summary']
        # depth = 1
        

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'picture']

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user