from django.db import models
from slugify import slugify

class AutoSlugMixin:
    """
    Automatically sets a slug field to a slugified version of any chosen
    naming field.
    """
    
    auto_slug_field = 'slug'
    auto_slug_populate_from = 'name'

    def hydrate_slug(self):
        # Skip if slug already set
        if getattr(self, self.auto_slug_field):
            return
        
        # Otherwise, set slugify populate field and update
        source = getattr(self, self.auto_slug_populate_from)
        if source:
            setattr(self, self.auto_slug_field, slugify(source))