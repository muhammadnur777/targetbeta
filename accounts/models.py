


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.timezone import now

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/%Y/%m/%d/',
        blank=True, null=True
    )

    def __str__(self):
        return self.get_full_name() or self.username

class UserReview(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField("Текст отзыва")
    rating  = models.PositiveSmallIntegerField("Оценка", default=5)
    posted  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted']
    def __str__(self):
        return f"{self.user.username}: {self.comment[:20]}…"
    

    @property
    def stars_range(self):
        """
        Вернёт range из 0 до rating, чтобы в шаблоне
        делать {% for _ in review.stars_range %}…{% endfor %}
        """
        return range(self.rating)
