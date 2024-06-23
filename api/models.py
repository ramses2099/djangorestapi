from django.db import models 

class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

# Create your models here.
class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=200)
    # relationship watchlist and streamplatform
    platform = models.ForeignKey(StreamPlatform, 
                                 on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title