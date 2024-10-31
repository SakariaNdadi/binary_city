from django import template


register = template.Library()


@register.simple_tag
def get_field_errors(form, field_name):
    if field_name in form.errors:
        return form.errors[field_name]
    return None


@register.filter
def queryset_to_dict_list(queryset):
    """
    Converts a queryset to a list of dictionaries.
    """
    if hasattr(queryset, "values"):
        return list(queryset.values())
    return []


@register.simple_tag(takes_context=True)
def rename(context, old_name, new_name):
    """Rename a variable in the context without changing its value."""
    if old_name in context:
        context[new_name] = context[old_name]
    return ""
