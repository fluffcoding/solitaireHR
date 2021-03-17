from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class Test(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser",email="test@example.com")
        user.set_password("testpassword")
        user.save()
    
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
