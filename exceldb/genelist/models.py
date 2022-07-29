from django.db import models

class Literature (models.Model):
    pmid = models.IntegerField(null=False)
    pmcid = models.CharField(max_length=10, null=False)
    doi = models.CharField(max_length=30, null=False)
    author = models.CharField(max_length=100)
    year = models.IntegerField
    journal = models.CharField(max_length=100)
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
      return self.author


class Gene (models.Model):
    sourcelink = models.ForeignKey(Literature, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    DIRECTNESS = [('DIRECT', 'DIRECT'), ('INDIRECT', 'INDIRECT')]
    gene = models.CharField(max_length=200, blank=False)
    directness = models.CharField(max_length=8, choices=DIRECTNESS, blank=False)
    mechanism = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    explanation = models.TextField()
    species = models.CharField(max_length=100)
    conclusions = models.TextField()
    zebra = models.URLField()

    def __str__(self):
     return self.gene




