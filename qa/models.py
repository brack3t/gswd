from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

from gswd.utils import get_redis_connection


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
        return self.title

    def save(self, *args, **kwargs):
        """
        Create the slug if not yet set.
        """
        if not self.slug:
            self.slug = slugify(self.title)

        super(Question, self).save(*args, **kwargs)

    @property
    def redis_key(self):
        return u"question:%d" % self.pk


class Answer(models.Model):
    """
    Answer model
    """
    user = models.ForeignKey(User, related_name="answers")
    question = models.ForeignKey(Question, related_name="answers")
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    accepted = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s - %s" % (self.user.get_full_name(), self.question.title)

    def save(self, *args, **kwargs):
        """
        If new answer, add answer to the zcard with a score of 0
        """
        create_key = False

        if not self.pk:
            create_key = True

        super(Answer, self).save(*args, **kwargs)

        if create_key:
            red = get_redis_connection()
            red.zadd(self.question.redis_key, 0, self.pk)

    @property
    def upvote(self):
        """
        Increment the answers score by 1
        """
        red = get_redis_connection()
        return red.zincrby(self.question.redis_key, self.pk, 1)

    @property
    def score(self):
        """
        Return the answer's score from Redis
        """
        red = get_redis_connection()
        return red.zscore(self.question.redis_key, self.pk)


class AnswerComment(models.Model):
    """
    Answer comment model
    """
    user = models.ForeignKey(User, related_name="comments")
    answer = models.ForeignKey(Answer, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
