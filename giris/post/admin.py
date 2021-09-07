from django.contrib import admin
from .models import Post
# from post.models import

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'slug'] # üstlerinde tarih ve detaylar çıkması postların
    list_display_links = ['publishing_date'] #üstlerine geldiğin zaman içine gitme
    list_filter = ['publishing_date'] #sağ tarafta tarih filtreleme
    search_fields = ['title', 'content'] #arama çubuğu
    list_editable = ['title']
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
