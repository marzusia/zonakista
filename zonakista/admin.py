from django.contrib import admin
from .models.citizens import Citizen
from .models.cities import City
from .models.articles import Article
from .models.organisation import Organisation

@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    pass