from django.contrib import admin
from .models.citizens import Citizen
from .models.cities import City
from .models.articles import Article
from .models.organisation import Organisation
from .models.lexicon import Word, Sense, Example, Gloss, Derivation

for model in [
    Citizen,
    City,
    Article,
    Organisation,
    Word,
    Sense,
    Example,
    Gloss,
    Derivation
]:
    admin.site.register(model)