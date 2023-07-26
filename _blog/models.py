from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)  # publish date
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    

    def get_absolute_url(self):
        # return reverse("article-detail", kwargs={"pk": self.pk})
        return reverse("article-detail", args=(str(self.id)))
    