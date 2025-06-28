# reviews/models.py

from django.db import models
from django.conf import settings

class Testimonial(models.Model):
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text       = models.TextField("Текст отзыва")
    rating     = models.PositiveSmallIntegerField("Оценка", default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.get_full_name()}: {self.text[:20]}…"



class contact(models.Model):
    name = models.CharField(max_length=500)
    phone = models.IntegerField()



                