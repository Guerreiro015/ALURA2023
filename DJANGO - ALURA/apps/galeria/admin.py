from django.contrib import admin

from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda","categoria",'publicar','usuario')
    list_display_links = ("id","nome","legenda","categoria")
    search_fields = ("nome",)
    list_filter = ("categoria","usuario",)
    list_per_page = 10
 
admin.site.register(Fotografia, ListandoFotografias)


