from django.db.models import Model, CharField, TextField, SlugField, ForeignKey, CASCADE
from django.utils.text import slugify
from mptt.fields import TreeForeignKey


class Category(Model):
    name = CharField(max_length=56)
    description = TextField()
    slug = SlugField()
    parent = TreeForeignKey('Category',
        related_name="products",
        on_delete=CASCADE)


    class Meta:
        db_table="category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug =slugify(self.slug)
        super().save(force_insert, force_update, using, update_fields)



