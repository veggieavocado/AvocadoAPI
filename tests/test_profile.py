from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class UserTestCase(TestCase):
    # maek user data
    def setUp(self):
        user, user_created = User.objects.get_or_create(username='test',
                                                        email="test@gmail.com",
                                                        password='test123123123')
        # Verify that user data has been created
        self.user = user
        self.assertTrue(user_created, msg='failed to save user data')
        self.assertEqual(User.objects.all().count(), 1, msg='user data not created properly')

    def test_user_is_created(self):
        username = self.user.username
        password = self.user.password
        email = self.user.email
        self.assertEqual(username, 'test')
        self.assertEqual(password, 'test123123123')
