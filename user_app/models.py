from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.user)

    def get_absolute_url(self):
        # return reverse('post_detail_view', args=(str(self.id)))
        return reverse('post')
