from django.test import TestCase
from services.models import Structure


class StructureTestCase(TestCase):
    # maek user data
    def setUp(self):
        structure, structure_created = Structure.objects.get_or_create(text=31012,
                                                                        sentence='25,35,44,88',
                                                                        role='인사하기,자료보여주기,중요부분강조,마무리',
                                                                        previous_state=1250,
                                                                        )
        # Verify that user data has been created
        self.assertTrue(structure_created, msg='failed to save user data')
        self.assertEqual(Structure.objects.all().count(), 1, msg='user data not created properly')

    def test_structure_is_created(self):
        self.structure_test = Structure.objects.all().first()
        text = self.structure_test.text
        sentence = self.structure_test.sentence
        role = self.structure_test.role
        previous_state = self.structure_test.previous_state
        self.assertEqual(text, 31012)
        self.assertEqual(sentence, '25,35,44,88')
        self.assertEqual(role, '인사하기,자료보여주기,중요부분강조,마무리')
        self.assertEqual(previous_state, 1250)
