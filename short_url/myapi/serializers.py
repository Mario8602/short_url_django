from rest_framework import serializers, status

from .models import Token


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('full_url', 'short_url', 'number_transitions', 'created_at', 'is_active')
        extra_kwargs = {'full_url': {'validators': []}}

    def create(self, validated_data):

        # token = Token()
        # token.full_url = validated_data.get('full_url', None)
        # token.short_url = Token.gen_token()
        # token.save()
        # return token

        full_url = validated_data['full_url']
        token, created = Token.objects.get_or_create(full_url=full_url)

        if created:
            status_code = status.HTTP_201_CREATED
        else:
            status_code = status.HTTP_200_OK

        return token, status_code