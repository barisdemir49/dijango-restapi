
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils import timezone


# Makale içerikleri için oluşturduğumuz Post tablo yapımız
class Post(models.Model):
    uuid=models.UUIDField(primary_key=True, default=uuid4,   editable=False )
    title =models.CharField( max_length=100, verbose_name="Makale Başlığı"  )
    slug =models.SlugField(unique=True, editable=False,  null=False, max_length=150 )
    content = RichTextField(verbose_name="Makale İçeriği", null=False )
    createDate=models.DateTimeField(auto_now_add=True,verbose_name="Makale Ekleme Tarihi")
    isActive=models.BooleanField(default=True, verbose_name="Makale Yayın Durumu")
    user=models.ForeignKey( User, on_delete=models.CASCADE, verbose_name="Makale Ekleyen" )
    draft=models.BooleanField(default=False,verbose_name="Taslaklara Kayıt Edilme Durumu")
    updateDate=models.DateTimeField(auto_now_add=True,verbose_name="Güncelleme Tarihi")
    image =models.ImageField(upload_to='media/post')

    class Meta:
        ordering =["-createDate"]
        
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if self.uuid:
            self.updateDate=timezone.now()
        self.slug=self.createSlug()
        return super(Post,self).save(*args,**kwargs)

    def createSlug(self):
        slug=slugify(self.title.replace('ı','İ'))
        slugUnique=slug
        i=1
        while Post.objects.filter(slug=slugUnique).exists():
            slugUnique='{}-{}'.format(slug,i)
            i+=1
        return slugUnique
    
