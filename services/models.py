from django.db import models

TYPES = (
    ('TEXT', '템플릿'),
    ('SENT', '문장'),
    ('WORD', '단어'),
)

STATUS_TYPES = (
    (1, 'pass'),
    (0, 'fail'),
)


class Sentence(models.Model):
    owner = models.CharField(max_length=4)
    userid = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    detail_role = models.CharField(max_length=100, blank=True, null=True)
    sentence = models.TextField(blank=True, null=True)
    translated = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.owner)

class Text(models.Model):
    owner = models.CharField(max_length=4)
    userid = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    template = models.TextField(blank=True, null=True)
    translated = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.owner)


class Word(models.Model):
    owner = models.CharField(max_length=4)
    userid = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    word = models.TextField(blank=True, null=True)
    translated = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.owner)


class State(models.Model):
    type = models.CharField(max_length=4, choices=TYPES, blank=True, null=True)
    status = models.BooleanField(choices=STATUS_TYPES)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return "{}".format(self.type)
