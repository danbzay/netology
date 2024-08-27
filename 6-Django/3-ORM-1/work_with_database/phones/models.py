from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=400, null=True)
    price = models.DecimalField(max_digits=10,  null=True, 
                                decimal_places=2)
    image = models.URLField( null=True)
    release_date = models.DateField(default='0000-00-00')
    lte_exists = models.BooleanField( null=True)
    slug = models.SlugField( null=True)
