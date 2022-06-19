from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.response import TemplateResponse

from actions.utils import get_followed_users_actions
from common.utils import get_paginator_if_page_correct


@login_required
def get_action_pagination(request):
    actions_paginator = get_paginator_if_page_correct(
        items_=get_followed_users_actions(request.user),
        per_page=settings.PAGINATION_PICTURES_AMOUNT,
        page=int(request.GET.get('page', 1)),
    )
    return (
        TemplateResponse(request, "actions/action_pagination.html", {"actions": actions_paginator}) if actions_paginator
        else HttpResponse('')
    )
