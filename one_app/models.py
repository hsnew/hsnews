from django.db import models


class News(models.Model):
    """Статья"""
    title = models.CharField("Заголовок", max_length=300)
    text = models.TextField("Тело")
    date = models.DateTimeField("дата", auto_now_add=True)
    picture = models.ImageField("Картинка", upload_to="images/", blank=True)
    chek = models.IntegerField("счетчик", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
