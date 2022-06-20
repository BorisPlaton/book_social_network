import redis
from django.conf import settings

from account.models import User
from actions.utils import create_action
from images.models import Image


r = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


def get_redis_image_total_views(image_pk: int) -> int:
    total_views: int = r.incr(f'image:{image_pk}:total_views')
    return total_views


def increase_image_ranking(image_pk: int):
    r.zincrby(f'image_rank', 1, image_pk)


def setup_additional_image_fields(user: User, image: Image):
    image.user = user
    image.save()
    create_action(user, "created image", target=image)


def like_image(image_id: int, action: str, user: User) -> bool:
    image = Image.objects.get(pk=image_id)
    match action:
        case "like":
            image.user_likes.add(user)
            create_action(user, "liked", target=image)
            return True
        case "unlike":
            image.user_likes.remove(user)
            return True
        case _:
            return False
