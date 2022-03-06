from django.db import models
from .base.abstracts import UpdatableModel
from .base.mixins import AutoSlugMixin


class Word(UpdatableModel, AutoSlugMixin):
    headword = models.CharField(
        max_length=255,
        unique=True,
        help_text='The dictionary form of the word'
    )
    pronunciation = models.CharField(
        max_length=255,
        blank=True,
        help_text='IPA for this word (do not include slashes or brackets)'
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=True,
        db_index=True,
        unique=True,
        help_text='How this word will appear in URLs. Leave blank to auto-generate.'
    )

    auto_slug_populate_from = 'headword'

    @property
    def all_senses(self):
        return Sense.objects.filter(word=self.id)

    def __str__(self):
        return self.headword


class Sense(models.Model):
    class PartOfSpeech:
        NOUN = 'noun'
        VERB = 'verb'
        ADJECTIVE = 'adjective'
        ADVERB = 'adverb'
        CONJUNCTION = 'conjunction'
        DETERMINER = 'determiner'
        INTERJECTION = 'interjection'
        PREPOSITION = 'preposition'
        PRONOUN = 'pronoun'
        PROPER_NOUN = 'proper noun'
        NUMERAL = 'numeral'
        CHOICES = (
            (NOUN, 'Noun'),
            (VERB, 'Verb'),
            (ADJECTIVE, 'Adjective'),
            (ADVERB, 'Adverb'),
            (CONJUNCTION, 'Conjunction'),
            (DETERMINER, 'Determiner'),
            (INTERJECTION, 'Interjection'),
            (PREPOSITION, 'Preposition'),
            (PRONOUN, 'Pronoun'),
            (PROPER_NOUN, 'Proper Noun'),
            (NUMERAL, 'Numeral'),
        )

    class WordGender:
        MASCULINE = 'masculine'
        FEMININE = 'feminine'
        CHOICES = (
            (MASCULINE, 'Masculine'),
            (FEMININE, 'Feminine'),
        )
    
    class WordClass:
        THEMATIC = 'thematic'
        ATHEMATIC = 'athematic'
        IRREGULAR = 'irregular'
        A_STEM = 'a-stem'
        I_STEM = 'i-stem'
        U_STEM = 'u-stem'
        R_STEM = 'r-stem'
        CHOICES = (
            (THEMATIC, 'Thematic'),
            (ATHEMATIC, 'Athematic'),
            (IRREGULAR, 'Irregular'),
            (A_STEM, 'a-stem'),
            (I_STEM, 'i-stem'),
            (U_STEM, 'u-stem'),
            (R_STEM, 'r-stem'),
        )

    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
        related_name='senses',
    )
    partOfSpeech = models.CharField(
        max_length=64,
        choices=PartOfSpeech.CHOICES,
    )
    gender = models.CharField(
        max_length=64,
        blank=True,
        choices=WordGender.CHOICES,
    )
    wordClass = models.CharField(
        max_length=64,
        blank=True,
        choices=WordClass.CHOICES,
    )
    alternative_to = models.ForeignKey(
        Word,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=(
            'If this word is an alternative form (e.g other gender '
            'or colloquial alternative) then include the main '
            'word here.'
        ),
        related_name='alternatives'
    )
    alternative_note = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            'A simple explanation of this alternative, e.g feminine'
        )
    )
    etymology_note = models.CharField(
        max_length=255,
        blank=True,
        help_text='Origin of this word',
    )
    source_language = models.CharField(
        max_length=64,
        blank=True,
        help_text=(
            'The language source of this word. Proto-Indo-European '
            'must be abbreviated to PIE. Do not use any other '
            'abbreviations. Leave blank if the word is derived '
            'from existing Vedian words.'
        )
    )
    pie_root = models.CharField(
        max_length=64,
        blank=True,
        help_text=(
            'The single PIE root this word stems from, '
            'if it is of native Vedian etymology.'
        )
    )
    notes = models.CharField(
        max_length=255,
        blank=True,
        help_text='Any other notes related to this sense.'
    )

    @property
    def all_glosses(self):
        return Gloss.objects.filter(sense=self.id)

    @property
    def all_examples(self):
        return Example.objects.filter(sense=self.id)

    def __str__(self):
        return '%s (%s)' % (
            self.word,
            self.partOfSpeech,
        )


class Gloss(models.Model):
    sense = models.ForeignKey(
        Sense,
        on_delete=models.CASCADE,
        related_name='glosses',
    )
    index = models.IntegerField(
        help_text='Which order in the sense this gloss should appear',
    )
    field = models.CharField(
        max_length=128,
        blank=True,
        help_text=(
            'A defining characteristic of this word or its usage, if '
            'applicable, e.g \'biology\' or \'colloquial\'.'
        )
    )
    gloss = models.CharField(
        max_length=255,
        help_text='The actual gloss'
    )

    def __str__(self):
        return '%s: %s' % (self.sense, self.gloss)

    class Meta:
        indexes = [
            models.Index(fields=['sense', 'index'])
        ]
        verbose_name_plural = 'Glosses'


class Example(models.Model):
    sense = models.ForeignKey(
        Sense,
        on_delete=models.CASCADE,
        related_name='examples',
    )
    sentence = models.CharField(
        max_length=255,
        help_text='The example sentence in Vedian.',
    )
    gloss = models.CharField(
        max_length=255,
        blank=True,
        help_text='Translation of the example sentence',
    )
    source = models.CharField(
        max_length=255,
        blank=True,
        help_text='If applicable, the source of the example.',
    )

    def __str__(self):
        return self.sentence


class Derivation(models.Model):
    sense = models.ForeignKey(
        Sense,
        on_delete=models.CASCADE,
        related_name='parent_terms',
    )
    derives_from = models.ForeignKey(
        Sense,
        on_delete=models.CASCADE,
        related_name='derived_terms',
    )

    def __str__(self):
        return '%s < %s' % (self.sense, self.derives_from)