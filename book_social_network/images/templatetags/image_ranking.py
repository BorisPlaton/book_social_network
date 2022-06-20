import redis
from django import template
from django.conf import settings

from images.models import Image


register = template.Library()
r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


@register.inclusion_tag('images/inclusion_tags/most_ranked_images.html')
def show_most_ranked_images(amount: int = 10):
    images_pk = [int(pk) for pk in r.zrange('image_rank', 0, -1, desc=True)[:amount]]
    images = list(Image.objects.filter(pk__in=images_pk))
    images.sort(key=lambda x: images_pk.index(x.pk))
    return {'images': images}
