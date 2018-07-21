from django.test import TestCase
from services.models import Sentence


class SentenceTestCase(TestCase):
    # maek user data
    def setUp(self):
        sentence, sentence_created = Sentence.objects.get_or_create(owner='VA',
                                                                    userid="1000",
                                                                    source='TED',
                                                                    role='프레젠테이션',
                                                                    detail_role='스티브잡스 연설',
                                                                    sentence='It started before I was born',
                                                                    translated='내가 태어나 기 전에 시작되었습니다.',
                                                                    )
        # Verify that user data has been created
        self.assertTrue(sentence_created, msg='failed to save user data')
        self.assertEqual(Sentence.objects.all().count(), 1, msg='user data not created properly')

    def test_user_is_created(self):
        self.sentence_test = Sentence.objects.all().first()
        owner = self.sentence_test.owner
        userid = self.sentence_test.userid
        source = self.sentence_test.source
        role = self.sentence_test.role
        detail_role = self.sentence_test.detail_role
        sentence = self.sentence_test.sentence
        translated = self.sentence_test. translated
        self.assertEqual(owner, 'VA')
        self.assertEqual(userid, 1000)
        self.assertEqual(source, 'TED')
        self.assertEqual(role, '프레젠테이션')
        self.assertEqual(detail_role, '스티브잡스 연설')
        self.assertEqual(sentence, 'It started before I was born')
        self.assertEqual(translated, '내가 태어나 기 전에 시작되었습니다.')
