from django import template
register = template.Library()

@register.filter
def find_replace(string, find_replace=",|"):
    find, replace = find_replace.split("|")
    return string.replace(',','')