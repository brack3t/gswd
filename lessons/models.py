from django.db import models
from django.template.defaultfilters import slugify

import misaka as mi

LANGUAGE_CHOICES = (
    ("en", "English"),
)


class Lesson(models.Model):
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    order = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, editable=False)
    video = models.URLField(blank=True, default='')

    class Meta:
        ordering = ["order", "title"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Lesson, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ("lessons:detail", (), {"slug": self.slug})


class Translation(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="transcripts")
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    intro = models.TextField()
    intro_html = models.TextField(blank=True, default='', editable=False)
    body = models.TextField()
    body_html = models.TextField(blank=True, default='', editable=False)
    transcript = models.TextField(blank=True)
    transcript_html = models.TextField(blank=True, default='', editable=False)

    def __unicode__(self):
        return '"%s" in %s' % (self.lesson.title, self.get_language_display())

    def save(self, *args, **kwargs):
        self.intro_html = mi.html(self.intro,
            extensions=mi.EXT_NO_INTRA_EMPHASIS | mi.EXT_FENCED_CODE | mi.HTML_HARD_WRAP)
        self.body_html = mi.html(self.body,
            extensions=mi.EXT_NO_INTRA_EMPHASIS | mi.EXT_FENCED_CODE | mi.HTML_HARD_WRAP)
        self.transcript_html = mi.html(self.transcript,
            extensions=mi.EXT_NO_INTRA_EMPHASIS | mi.EXT_FENCED_CODE | mi.HTML_HARD_WRAP)
        super(Translation, self).save(*args, **kwargs)
