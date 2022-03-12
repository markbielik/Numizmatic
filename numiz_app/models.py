from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

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
                            max_length=100)

    def __str__(self):
        return f"{self.name}"


class Coin(models.Model):
    title = models.CharField(verbose_name="Coin title",
                             max_length=128,
                             null=False)
    category = models.ForeignKey("Category",
                                 on_delete=models.CASCADE,
                                 null=False)
    designer = models.ManyToManyField(Designer)
    issuer = models.ForeignKey('Issuer',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=False)
    subject = models.ForeignKey('Subject',
                                on_delete=models.CASCADE,
                                default='individual subject')
    description = models.TextField(verbose_name="Coin description")
    stamp = models.CharField(choices=TYPE_STAMP,
                             max_length=15)
    attempt = models.CharField(verbose_name="Coin attempt",
                               max_length=100)
    reverse = models.ImageField(verbose_name="Coin reverse")
    obverse = models.ImageField(verbose_name="Coin obverse")
    issue_date = models.DateTimeField(default=timezone.now)
    circulation = models.IntegerField()
    dimension = models.DecimalField(max_digits=4,
                                    decimal_places=2,
                                    help_text="Dimension coin in milimeters")
    scales = models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 help_text="Scales coin in grams")
    remarks = models.CharField(verbose_name="Remarks for coin",
                               max_length=200)
    tag = models.ManyToManyField("Tag")
    slug = models.SlugField()
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('coin_detail_view', args=(self.pk, ))


class Issuer(models.Model):
    name = models.CharField(verbose_name="Name of issuer",
                            max_length=250,
                            null=False)
    description = models.TextField()
    short_name = models.CharField(verbose_name="Short name of issuer",
                                  max_length=5)

    def __str__(self):
        return f"{self.name}"


class Subject(models.Model):
    name = models.CharField(verbose_name="Subject name",
                            max_length=250)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(verbose_name="Tag name",
                            max_length=50)

    def __str__(self):
        return f"{self.name}"
