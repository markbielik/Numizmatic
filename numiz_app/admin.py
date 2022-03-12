from django.contrib import admin

from numiz_app.models import Designer, Coin, Issuer, Tag, Category, Subject

admin.site.register(Designer)
admin.site.register(Coin)
admin.site.register(Issuer)
admin.site.register(Subject)
admin.site.register(Tag)
admin.site.register(Category)

