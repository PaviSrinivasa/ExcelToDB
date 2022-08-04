from django.db import models
from django import forms
from .models import Gene, Literature

class Literatureform(forms.ModelForm):
    class Meta:
        model = Literature
        fields = '__all__'
        labels = {'pmid':'What is the pmid?',
                  'pmcid':'What is the pmcid?',
                  'doi':'What is the DOI?',
                  'author':'What is the name of the author?',
                  'year': 'In which year was it published?',
                  'journal': 'What is the journal?',
                  'title':'What is the title of the Literature?',
                  'description':'How do you describe this Literature?',
                  }

class Geneform(forms.ModelForm):
    sourcelink_id = forms.ModelChoiceField(queryset=Literature.objects.all())

    # def save(self, commit=True):
    #    instance = super(Geneform, self).save(commit=False)
    #    lit = self.cleaned_data['litobj']
    #    instance.litobj = lit[0]
    #    instance.save(commit)
    #    return instance

    class Meta:
        model = Gene
        fields = ('gene','sourcelink_id','directness','mechanism','method','explanation','species','conclusions','zebra')
        labels = {
                  'gene':'What kind of gene?',
                  'sourcelink_id':'What is the source?',
                  'directness':'What is the directness?',
                  'mechanism':'Which mechanism was used?',
                  'method': 'Which method was used?',
                  'explanation': 'Can you provide more explanation?',
                  'species':'What kind of species?',
                  'conclusions':'What are the conclusions?',
                  'zebra':'What is the zebrafinchatlas link?',
                  }
