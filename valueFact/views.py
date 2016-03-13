from rest_framework import permissions, viewsets
from rest_framework.response import Response

from valueFact.models import ValueFactPost
from valueFact.serializers import ValueFactPostSerializer
from valueFact.permissions import IsAuthorOfValueFact


class ValueFactViewSet(viewsets.ModelViewSet):
    queryset = ValueFactPost.objects.order_by('-created_date')
    serializer_class = ValueFactPostSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfValueFact(),)


def perform_create(self, serializer):
    instance = serializer.save(author=self.request.user) #is it user?

    return super(ValueFactViewSet, self).perform_create(serializer)


class AccountPostsViewSet(viewsets.ViewSet):
    #Change to view for a specific stock and segment
    queryset = ValueFactPost.objects.select_related('author').all()
    serializer_class = ValueFactPostSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
