from django import template
# Custom template tag for indexing a list in Jinja
# Credit for code goes to https://djangosnippets.org/snippets/2740/
register = template.Library()


@register.filter
def get_at_index(list, index):
    '''Return the list element at the given index.'''
    return list[index]


@register.filter
def subtract_one(length):
    '''Subtract one from int:length and return the difference.'''
    return length - 1
