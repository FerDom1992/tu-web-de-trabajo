from django.db import models

class PostCh(models.Model):
    titulo  = models.CharField(verbose_name = 'Título', max_length = 200)
    imagen  = models.ImageField(verbose_name = 'Imagen', upload_to = '', blank = True, null = True)
    mensaje = models.TextField(verbose_name = 'Mensaje')
    created = models.DateTimeField(verbose_name = 'Fecha de creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha de edición', auto_now = True)

    class Meta:
        ordering = ['created', 'updated']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo