from django.db import models

# Write your models here

#* Song model should:
#  * have a title
#  * have an artist (original performer)
#  * have a performer (who's singing it for karaoke) (make this another model)
#  * have a length (number of seconds in duration)
#  * return '<title> by <artist>' when turned into a string
#  
#* Performer model should:
#  * have a name
#  * return the name when turned into a string

class Performer(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    performer = models.ForeignKey(Performer)
    length = models.IntegerField(default=0)
    
    def __str__(self):
        return "{} by {}".format(self.title, self.artist)
    
