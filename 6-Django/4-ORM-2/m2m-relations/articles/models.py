from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='тэг')

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(
        Tag, 
        through='Scope', 
        through_fields=('article', 'tag')
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, 
        related_name='scopes', 
        on_delete=models.CASCADE
    )
    is_main = models.BooleanField(default=False)


