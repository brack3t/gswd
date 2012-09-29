from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Question(models.Model):
    """
    Question model
    """
    user = models.ForeignKey(User, related_name="questions")
    title = models.CharField(max_length=255)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(db_index=True, editable=False, max_length=255)

    def __unicode__(self):
        return u"%s" % self.title

    def save(self, *args, **kwargs):
        """
        Create the slug if not yet set.
        """
        if not self.slug:
            self.slug = slugify(self.title)

        super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    """
    Answer model
    """
    user = models.ForeignKey(User, related_name="answers")
    question = models.ForeignKey(Question, related_name="answers")
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class AnswerComment(models.Model):
    """
    Answer comment model
    """
    user = models.ForeignKey(User, related_name="comments")
    answer = models.ForeignKey(Answer, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
