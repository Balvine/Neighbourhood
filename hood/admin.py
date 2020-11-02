from django.contrib import admin
from .models import Neighborhood,UserProfile,Company,Post,Comment,Location,Category
# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Location)
admin.site.register(Category)
