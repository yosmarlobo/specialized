from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    name = models.CharField(
        _("nombre"),
        max_length=50
    )
    author = models.CharField(
        _("Autor"),
        max_length=50
    )
    description = models.TextField(
        _("Descripcion")
    )
    image = models.ImageField(
        _("Imagen"),
        upload_to="imagen/blog"
    )

    create_at = models.DateTimeField(
        _("Fecha de creacion"),
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        _("Fecha de actualizacion"),
        auto_now=True
    )

    class Meta:
        verbose_name = _("Blog Personal")
        verbose_name_plural = _("Blogs Personales")
        ordering = ["name"]

    def __str__(self):
        return self.name
