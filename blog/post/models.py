from logging import root
from pyexpat import model
from uuid import uuid4
from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Makale içerikleri için oluşturduğumuz Post tablo yapımız
class Post(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid4,   editable=False )
    title =models.CharField( max_length=100, verbose_name="Makale Başlığı"  )
    slug =models.SlugField(unique=True, editable=False,  null=False, max_length=150 )
    content = RichTextField(verbose_name="Makale İçeriği", null=False )
    createDate=models.DateTimeField(auto_now_add=True,verbose_name="Makale Ekleme Tarihi" )
    isActive=models.BooleanField(default=True, verbose_name="Makale Yayın Durumu")
    user=models.ForeignKey( User, on_delete=models.CASCADE, verbose_name="Makale Ekleyen" )

    class Meta:
        ordering =["-createDate"]
        
    def __str__(self) -> str:
        return self.title
    
    def createSlug(self):
        slug=slugify(self.title.replace('ı','İ'))
        slugUnique=slug
        i=1
        while Post.objects.filter(slug=slugUnique).exists():
            slugUnique='{}-{}'.format(slug,i)
            i+=1
        return slugUnique
    
