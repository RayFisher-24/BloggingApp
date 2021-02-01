from django.contrib import admin
from .models import photo
from .models import wedding
from .models import Contact
from .models import Article
# Register your models here.

admin.site.register(photo)
admin.site.register(wedding)
admin.site.register(Contact)
admin.site.register(Article)
