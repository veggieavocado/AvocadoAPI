from django.test import TestCase
from services.models import Text


class TextTestCase(TestCase):
    # maek user data

    def setUp(self):
        self.example = "It started before I was born. My biological mother was a young, unwed college graduate student,and she decided to put me up for adoption.\
                         She felt very strongly that I should be adopted by college graduates,so everything was all set for me to be adopted at birth by a lawyer and his wife. \
                         Except that when I popped out they decided at the last minute that they really wanted a girl. So my parents, who were on a waiting list, \
                         got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.”\
                         My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school.\
                         She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college."

        text, text_created = Text.objects.get_or_create(owner='VA',
                                                        userid="1000",
                                                        type="e-mail",
                                                        source='book',
                                                        category='business',
                                                        title='스티브잡스 연설',
                                                        template=self.example ,
                                                        translated=self.example,
                                                        )
        # Verify that user data has been created
        self.assertTrue(text_created, msg='failed to save user data')
        self.assertEqual(Text.objects.all().count(), 1, msg='user data not created properly')

    def test_text_is_created(self):
        self.texts_test = Text.objects.all().first()
        owner = self.texts_test.owner
        userid = self.texts_test.userid
        type = self.texts_test.type
        source = self.texts_test.source
        category = self.texts_test.category
        title = self.texts_test.title
        template = self.texts_test.template
        translated = self.texts_test.translated
        self.assertEqual(owner, 'VA')
        self.assertEqual(userid, 1000)
        self.assertEqual(type, 'e-mail')
        self.assertEqual(source, 'book')
        self.assertEqual(category, 'business')
        self.assertEqual(title, '스티브잡스 연설')
        self.assertEqual(template, self.example)
        self.assertEqual(translated, self.example)
