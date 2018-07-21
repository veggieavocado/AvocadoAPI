from django.test import TestCase
from services.models import State


class StateTestCase(TestCase):
    # maek user data
    def setUp(self):
        state, state_created = State.objects.get_or_create(type="text",
                                                           status=1)
        # Verify that user data has been created
        self.assertTrue(state_created, msg='failed to save user data')
        self.assertEqual(State.objects.all().count(), 1, msg='user data not created properly')

    def test_user_is_created(self):
        self.state_test = State.objects.all().first()
        type = self.state_test.type
        status = self.state_test.status
        self.assertEqual(type, 'text')
        self.assertEqual(status, 1)
