from django.contrib import admin
from .models.citizens import Citizen
from .models.cities import City
from .models.articles import Article
from .models.organisation import Organisation
from .models.lexicon import Word, Sense, Example, Gloss, Derivation

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

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass

@admin.register(Sense)
class SenseAdmin(admin.ModelAdmin):
    pass

@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    pass

@admin.register(Gloss)
class GlossAdmin(admin.ModelAdmin):
    pass

@admin.register(Derivation)
class DerivationAdmin(admin.ModelAdmin):
    pass
