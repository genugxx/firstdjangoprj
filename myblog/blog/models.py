from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self): # shell -> [뜯어온 자료].publish()
        self.publish_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title
    
# get은 1개의 자료만, filter는 조건에 맞는 자료 모두.
