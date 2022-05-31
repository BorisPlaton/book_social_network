from django import template


register = template.Library()


@register.inclusion_tag('account/inclusion_tags/text_input.html')
def text_input(field, **kwargs):
    attrs = {
        'class': 'form-control' + field.field.widget.attrs.pop('class', ''),
        **field.field.widget.attrs,
    }

    for key, value in kwargs.items():
        if key in attrs:
            attrs[key] += f' {value}'
        else:
            attrs[key] = str(value)

    field.field.widget.attrs.update(attrs)
    return {'field': field}
