from .models import User
from django.conf import settings
from django.templatetags import static
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'birthday',
            'country',
            'avatar',
            'first_name',
            'last_name',
            'reviews_number',
            'is_subscribed',
            'user_permissions_category'
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_avatar(self, obj):
        url = obj.avatar.url if obj.avatar else static(settings.BLANK_PHOTO)
        request = self.context.get("request", None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url
