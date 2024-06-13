from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField('date published')

    def __str__(self):
        return self.name

    
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=30)
    text = models.TextField()
    date_create = models.DateField('data created')

    def __str__(self):
          return f'Comment by {self.author} on Post "{self.post.name}"'



