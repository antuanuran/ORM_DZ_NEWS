from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    # ссылка m-to-m  на "articles"
    # ссылка 1-to-m  на "scopes"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, related_name='articles', through='Scope')        #Ссылка m-to-m (Article - Tag) но через дополнительную таблицу Scope
    # ссылка 1-to-m на "scopes"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


# создаем промежуточную таблицу для связи m-to-m (Tag и Article) для того, чтобы добавить доп.параметр is_main
class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_main', 'tag__name']
