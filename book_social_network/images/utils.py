from account.models import User
from actions.utils import create_action
from images.models import Image


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
