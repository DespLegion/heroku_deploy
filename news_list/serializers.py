from rest_framework import serializers
from .models import News


class NewsListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = News
        fields = ('sh_name', 'category')


class DetailNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('id', 'sh_name', 'category',)