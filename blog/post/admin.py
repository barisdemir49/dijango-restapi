from django.contrib import admin
from post.models import Post

# Modelimizi admin panelinde de yönetilmesi için
admin.site.register(Post)


#Makaleleri admin panelinde listelerken görünecek alanları ve filtrelemeleri gösterelim
class PostAdmin(admin.ModelAdmin):
    list_display=["title","user","createdDate","isActive"]
    search_fields=["title","content"]
    list_filter=["createdDate"]
    
    class Meta:
        model=Post