from rest_framework import serializers, status

from .models import Token


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = '__all__'
        # fields = ('full_url', 'short_url', 'number_transitions', 'created_at', 'is_active')
        extra_kwargs = {'full_url': {'validators': []}}

    def create(self, validated_data):

        print(validated_data)
        
        if 'short_url' in validated_data:
            full_url = validated_data['full_url']
            short_url = validated_data['short_url']
            token, created = Token.objects.get_or_create(full_url=full_url, short_url=short_url)
        else:
            full_url = validated_data['full_url']
            token, created = Token.objects.get_or_create(full_url=full_url)

        if created:
            status_code = status.HTTP_201_CREATED
        else:
            status_code = status.HTTP_200_OK

        return token, status_code