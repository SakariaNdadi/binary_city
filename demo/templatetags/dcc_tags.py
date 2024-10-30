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
