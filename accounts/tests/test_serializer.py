from django.test import TestCase
#from django.contrib.auth import get_user_model
from accounts.models import User
from accounts.serializers import UserSerializer

#User=get_user_model()

class JSONSerializerTest(TestCase):

    def test_serializer(self):

        #Initialize
        a = User.objects.create_user('test@test.com', username='test')
        serialized_account = UserSerializer(a)
        email = serialized_account.data.get('email')
        username = serialized_account.data.get('username')

        #test
        self.assertIn('test@test.com', email)
        self.assertIn('test', username)







