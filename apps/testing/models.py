from django.db import models

class Question(models.Model):
    question=models.TextField()
    image = models.ImageField(upload_to='media/')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    answer=models.TextField()
    boolean_field = models.BooleanField()






