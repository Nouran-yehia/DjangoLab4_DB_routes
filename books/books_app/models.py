from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(max_length=100)
    image = models.FileField(max_length=50, default='img.jpg')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



