from django import template

register=template.Library()

@register.simple_tag(name='getstatus')
def getstatus(status):
    status_array=['No Information','Confirmed','Processed','Delivered','Rejected']
    return status_array[status]