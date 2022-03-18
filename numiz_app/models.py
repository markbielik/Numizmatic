from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

TYPE_STAMP = (
    ('simple', 'Simple'),
    ('3d', '3D'),
    ('mirror', 'Mirror'),
)


class Designer(models.Model):
    first_name = models.CharField(verbose_name="Designer first name",
                                  max_length=100)
    last_name = models.CharField(verbose_name="Designer surname",
                                 max_length=150)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(verbose_name="Category name",
                            max_length=100,
                            unique=True)
    description = models.TextField(verbose_name="About of category",
                                   blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('name', )

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('category_detail', args=(self.pk, ))

    def get_update_url(self):
        return reverse('category_update', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('category_del', args=(self.pk, ))


class Coin(models.Model):
    title = models.CharField(verbose_name="Coin title",
                             max_length=128,
                             null=False)
    category = models.ForeignKey("Category",
                                 on_delete=models.CASCADE,
                                 related_name='coins',
                                 null=False)
    designer = models.ManyToManyField(Designer)
    issuer = models.ForeignKey('Issuer',
                               on_delete=models.CASCADE,
                               null=False)
    subject = models.ForeignKey('Subject',
                                on_delete=models.CASCADE,
                                help_text='If there is no topic, choose an individual topic')
    face_value = models.ForeignKey('Currency',
                                   on_delete=models.CASCADE,
                                   default=None,
                                   null=False)
    description = models.TextField(verbose_name="Coin description")
    stamp = models.CharField(choices=TYPE_STAMP,
                             max_length=15)
    attempt = models.CharField(verbose_name="Coin attempt",
                               max_length=100)
    obverse = models.ImageField(verbose_name="Coin obverse",
                                upload_to='obverse/%Y/%m',
                                blank=True)
    reverse = models.ImageField(verbose_name="Coin reverse",
                                upload_to='reverse/%Y/%m',
                                blank=True)
    issue_date = models.DateField()
    circulation = models.IntegerField(help_text="mintage in the number of pieces")
    dimension = models.DecimalField(max_digits=6,
                                    decimal_places=2,
                                    help_text="dimension coin in milimeters")
    scales = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 help_text="scales coin in grams")
    remarks = models.CharField(verbose_name="remarks for coin",
                               max_length=200,
                               null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200,
                            unique_for_date='created')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('coin_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('coin_update', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('coin_del', args=(self.pk, ))


class Issuer(models.Model):
    name = models.CharField(verbose_name="Name of issuer",
                            max_length=250,
                            null=False)
    description = models.TextField()
    short_name = models.CharField(verbose_name="Short name of issuer",
                                  max_length=5)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('issuer_detail', args=(self.pk, ))

    def get_update_url(self):
        return reverse('issuer_update', args=(self.pk, ))

    def get_delete_url(self):
        return reverse('issuer_del', args=(self.pk, ))


class Subject(models.Model):
    name = models.CharField(verbose_name="Subject name",
                            max_length=250,
                            default="Temat indywidualny",
                            unique=True)
    description = models.TextField(verbose_name="Description of subject",
                                   blank=True)

    def __str__(self):
        return f"{self.name}"


TYPE_UNIT = (
    ('pln', 'PLN'),
    ('euro', 'EURO'),
    ('usd', 'USD'),
    ('aud', 'AUD'),
    ('gbp', 'GBP'),
    ('chf', 'CHF')
)


class Currency(models.Model):
    value = models.IntegerField(verbose_name="Coin face value",
                                unique=True)
    unit = models.CharField(choices=TYPE_UNIT,
                            max_length=5)

    def __str__(self):
        return f"{self.value} {self.unit}"

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'
        ordering = ('value', )
