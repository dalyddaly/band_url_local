from django.contrib import admin
from products.models import Product
from models import Post

admin.site.register(Post)

admin.site.register(Product)
