from django.contrib import admin

from numiz_app.models import Designer, Coin, Issuer, Category, Subject, Currency

admin.site.register(Category)


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'slug', 'created', 'updated')
    search_fields = ('title', 'subject')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('user', )
    date_hierarchy = 'created'


admin.site.register(Designer)
admin.site.register(Issuer)
admin.site.register(Subject)
admin.site.register(Currency)


