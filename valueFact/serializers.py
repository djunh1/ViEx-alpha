from rest_framework import serializers

from accounts.serializers import UserSerializer
from valueFact.models import ValueFactPost

class ValueFactPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True, required=False)

    class Meta:
        model = ValueFactPost

        fields = ('author', 'text', 'created_date', 'score' )
        read_only_fields=('created_date', 'score')

    def get_validation_exclusions(self,*args, **kwargs):
        exclusions = super(UserSerializer,self).get_validation_exclusions()

        return exclusions + ['author']