from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(
        get_user_model(), related_name='images_created', on_delete=models.CASCADE, verbose_name='author'
    )
    title = models.CharField("Image title", max_length=128)
    slug = models.SlugField("Image slug", blank=True)
    image = models.ImageField("Picture", upload_to='images/%Y/%m/%d/')
    description = models.TextField(max_length=512, blank=True)
    created = models.DateTimeField("Created at", auto_now_add=True, db_index=True)
    user_likes = models.ManyToManyField(
        get_user_model(), related_name='liked_images', verbose_name='likes', blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:image_details', args=[self.pk, self.slug])

    def __str__(self):
        return self.title
