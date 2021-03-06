from django.db import models
from aweach.users import models as user_models

# Create your models here.


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)


class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, on_delete=models.PROTECT)

    def __str__(self):
        return self.message


class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}'.format(self.creator.username, self.image.caption)
