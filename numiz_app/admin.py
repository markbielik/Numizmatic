from django.contrib import admin

from numiz_app.models import Designer, Coin, Issuer, Category, Subject, Currency

admin.site.register(Designer)
admin.site.register(Coin)
admin.site.register(Issuer)
admin.site.register(Subject)
admin.site.register(Currency)
admin.site.register(Category)

