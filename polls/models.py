from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey


class slideshow(models.Model):
    id= models.AutoField(auto_created=True,primary_key=True,serialize=False)
    slideshow_first_image=models.ImageField(upload_to='img/slide',blank=True,verbose_name='Slide show birinci sekil')
    slideshow_second_image=models.ImageField(upload_to='img/slide',blank=True,verbose_name='Slide show ikinci sekil')
    slideshow_first_h1=models.CharField(max_length=250,verbose_name='Slide show birinci basliq')
    slideshow_first_p=models.CharField(max_length=250,verbose_name='Slide show birinci metin')
    slideshow_second_h1=models.CharField(max_length=250,verbose_name='Slide show ikinci basliq')
    slideshow_second_p=models.CharField(max_length=250,verbose_name='Slide show ikinci metin')

    def __str__(self):
        return self.slideshow_first_p




class tablecell(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    tablecell_first_h4=models.CharField(max_length=250,verbose_name='Slide show birinci basliq')
    tablecell_second_h4=models.CharField(max_length=250,verbose_name='Slide show ikinci basliq')
    tablecell_first_h3=models.CharField(max_length=250,verbose_name='Slide show birinci kicik basliq')
    tablecell_second_h3=models.CharField(max_length=250,verbose_name='Slide show ikinci kicik basliq')
    tablecell_second_p=models.CharField(max_length=250,verbose_name='Slide show ikinci metin')
    tablecell_first_p=models.CharField(max_length=250,verbose_name='Slide show birinci metin')
    tablecell_first_img=models.ImageField(upload_to='img/banner',verbose_name='Slide show birinci sekil')
    tablecell_second_img=models.ImageField(upload_to='img/banner',verbose_name='Slide show ikinci sekil')

    def __str__(self):
        return self.tablecell_first_h4


class product_image(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True,serialize=False)
    product_image_name = models.CharField(max_length=250, verbose_name='Sekilin adi')
    product_image=models.ImageField(upload_to='img',verbose_name='Sekil')
    product_image_sale=models.CharField(max_length=250,verbose_name='Satis qiymeti')
    product_image_discount=models.CharField(max_length=250, verbose_name='Endirim',null=True)
    product_image_new=models.CharField(max_length=250,verbose_name='Yeni?',null=True)
    product_image_stock=models.CharField(max_length=250,verbose_name='Stokda?',null=True)
    product_image_second_discount=models.CharField(max_length=250, verbose_name='Endirimden sonraki qiymeti',null=True)

    def __str__(self):
        return self.product_image_name

class comments(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    pict_id = models.ImageField(upload_to='img',verbose_name='sekil id')
    user_id = models.CharField(max_length=20,verbose_name='user id')
    body = models.TextField(verbose_name='Comments')

    def __str__(self):
        return self.body

"""
# Create your models here.

class product_image(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True,serialize=False)
    product_image_name=models.ImageField(upload_to='img',verbose_name='Sekilin adi')
    product_image_sale=models.CharField(max_length=250,verbose_name='Satis qiymeti')
    product_image_discount=models.CharField(max_length=250, verbose_name='Endirim')
    product_image_new=models.ImageField(upload_to='img',verbose_name='Yeni sekil')
    product_image_stock=models.CharField(max_length=250,verbose_name='Stokda?')
    product_image_link=models.CharField(max_length=250, verbose_name='Sekil linki')
    product_image_second_discount=models.CharField(max_length=250, verbose_name='Endirimden sonraki qiymeti')


    def __str__(self):
        return self.product_image_name



class comments(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    pict_id = models.CharField(max_length=20,verbose_name='sekil id')
    user_id = models.CharField(max_length=20,verbose_name='user id')
    body = models.TextField(verbose_name='Comments')

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        pass


class gul(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True,serialize=False)
    name = models.CharField(max_length=250, verbose_name='Ad')
    price = models.CharField(max_length=250, verbose_name='Qiymet')
    discount = models.CharField(max_length=250, verbose_name='Endirim')

    def __str__(self):
        return self.name




class posts(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    #kat_id = models.ForeignKey(Kategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name='Başlıq')
    body = models.TextField(verbose_name="M")
    posts_img_link = models.ImageField(upload_to='img',blank=True,verbose_name='Şəkil')
    created_at = models.DateTimeField(verbose_name='İndiki vaxt')

    def __str__(self):
        return self.title







class users(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    name=models.CharField(max_length=250, verbose_name='Istifadeci adi')
    email=models.CharField(max_length=250, verbose_name='Istifadeci emaili')

    def __str__(self):
        return self.email """










