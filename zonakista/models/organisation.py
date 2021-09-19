from django.db import models
from .base.abstracts import UpdatableModel

class Organisation(UpdatableModel):
    class Sectors:
        GOVERNMENT = 'government'
        TECHNOLOGY = 'technology'
        COMMERCE = 'commerce'
        INSURANCE = 'insurance'
        EDUCATION = 'education'
        HEALTHCARE = 'healthcare'
        MANUFACTURING = 'manufacturing'
        MINING = 'mining'
        CONSTRUCTION = 'construction'
        TRAVEL = 'travel'
        CHOICES = (
            (GOVERNMENT, 'Srayarda'),
            (TECHNOLOGY, 'Dali'),
            (COMMERCE, 'Tezara'),
            (INSURANCE, 'Krasalma'),
            (EDUCATION, 'Mantra'),
            (HEALTHCARE, 'Krarupa'),
            (MANUFACTURING, 'Busma'),
            (MINING, 'Ipulsa'),
            (CONSTRUCTION, 'Cinam'),
            (TRAVEL, 'Lugrunda'),
        )

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    sector = models.CharField(max_length=64, choices=Sectors.CHOICES)

    def __str__(self):
        return self.name