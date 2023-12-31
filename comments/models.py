from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return self.text