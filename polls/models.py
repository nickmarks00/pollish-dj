from django.core.validators import MinValueValidator
from django.db import models
from users.models import Profile

# Create your models here.
class Poll(models.Model):
    profile = models.ForeignKey(Profile, related_name='polls', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    question_text = models.TextField(blank=False, default="")

    def __str__(self):
        return f"{self.question_text} by {self.profile.user.username}"

    class Meta:
        unique_together = ['profile', 'created']  # user cannot create multiple posts at the same time
        ordering = ['-updated']  # default ordering for posts is time of last update
  

class Choice(models.Model):
    choice_image = models.ImageField(blank=True, upload_to="poll_directory_path", null=True)
    choice_text = models.CharField(max_length=255, blank=False, default="")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    profiles = models.ManyToManyField(Profile, related_name='choices')
    votes = models.IntegerField(default=0, blank=False, validators=[MinValueValidator(0)])

    # specifies upload path for poll images
    def poll_directory_path(self, filename):
        return f'user_{self.poll.profile.id}/poll_{self.poll.id}/{filename}'

    def __str__(self):
        return "{} --- {}".format(self.poll.question_text,self.choice_text)


class Comment(models.Model):
    comment_text = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    
