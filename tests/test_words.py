from django.test import TestCase
from services.models import Word


class SentenceTestCase(TestCase):
    # maek user data
    def setUp(self):
        word, word_created = Word.objects.get_or_create(owner='VA',
                                                        username='',
                                                        source='TED',
                                                        role='프레젠테이션',
                                                        word='speak',
                                                        translated='말하다',
                                                        )
        # Verify that user data has been created
        self.assertTrue(word_created, msg='failed to save user data')
        self.assertEqual(Word.objects.all().count(), 1, msg='user data not created properly')

    def test_word_is_created(self):
        self.word_test = Word.objects.all().first()
        owner = self.word_test.owner
        username = self.word_test.username
        source = self.word_test.source
        role = self.word_test.role
        word = self.word_test.word
        translated = self.word_test. translated
        self.assertEqual(owner, 'VA')
        self.assertEqual(username, '')
        self.assertEqual(source, 'TED')
        self.assertEqual(role, '프레젠테이션')
        self.assertEqual(word, 'speak')
        self.assertEqual(translated, '말하다')
