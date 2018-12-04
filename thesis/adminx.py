import xadmin
from .models import Tag, Thesis

class ThesisAdmin(object):
    list_display = ['title', 'pub_date', 'publisher', 'is_choiced', \
                    'tags', 'need_verify', 'getCollege']
    list_filter = ['title', 'is_choiced', 'tags', 'need_verify', \
                    'publisher__teacher__college','pub_date',]
    search_fields =['title',  'publisher__teacher__name']
    list_editable = ['need_verify']
    model_icon = 'fa fa-book'

class TagAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    model_icon = 'fa fa-tags'


xadmin.site.register(Thesis, ThesisAdmin)
xadmin.site.register(Tag, TagAdmin)
