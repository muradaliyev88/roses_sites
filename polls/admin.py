from django.contrib import admin
from .models import tablecell,slideshow,product_image,comments
from django.db import models

# Register your models here.


class tablecellAdmin(admin.ModelAdmin):
    list_display = ['tablecell_first_h4','tablecell_second_h4','tablecell_first_h3']
    list_display_links = ['tablecell_first_h4', 'tablecell_first_h3']
    list_filter = ['tablecell_first_h3']
    search_fields = ['tablecell_first_h4', 'tablecell_first_h3']



    class Meta:
        model = tablecell

class slideshowAdmin(admin.ModelAdmin):
    list_display = ['slideshow_first_h1','slideshow_first_p','slideshow_second_h1','slideshow_second_p']
    list_display_links = ['slideshow_first_h1', 'slideshow_second_h1']
    list_filter = ['slideshow_first_h1','slideshow_second_h1']
    search_fields = ['slideshow_second_h1', 'slideshow_first_h1']

    class Meta:
        model = slideshow


class product_imagesAdmin(admin.ModelAdmin):
    list_display = ['product_image_name']
    list_display_links = ['product_image_name']
    list_filter = ['product_image_name']
    search_fields = ['product_image_name']

    class Meta:
        model = product_image

class comAdmin(admin.ModelAdmin):
    list_display = ['body']
    list_display_links = ['body']
    list_filter = ['body']
    search_fields = ['body']

    class Meta:
        model = comments


admin.site.register(tablecell,tablecellAdmin)
admin.site.register(slideshow,slideshowAdmin)
admin.site.register(product_image,product_imagesAdmin)
admin.site.register(comments,comAdmin)