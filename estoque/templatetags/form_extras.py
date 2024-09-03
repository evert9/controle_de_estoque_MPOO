from django import template

register = template.Library()


@register.simple_tag
def input_with_classes(field, css_classes):
    css_classes = css_classes if css_classes else "form-control"
    if 'class' in field.field.widget.attrs:
        field.field.widget.attrs['class'] += ' ' + ''.join(css_classes)
    else:
        field.field.widget.attrs['class'] = ''.join(css_classes)
    return field
