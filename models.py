from django.db import models
from django.contrib.auth.models import User

#assign a word to a player
class word(models.Model):
    wordName=models.CharField(max_length=200)
    wordDif=models.ForeignKey('difficulty',on_delete=models.CASCADE,null=False)
    wordLen=models.PositiveIntegerField()
    user=models.ForeignKey(User, to_field="username",on_delete=models.CASCADE)
    def _str_(self):
        return self.wordName

#table containing diffs and their word lengths
class difficulty(models.Model):
    diffName=models.CharField(max_length=200)
    wordLenMin=models.PositiveIntegerField()
    wordLenMax=models.PositiveIntegerField()
    def _str_(self):
        return self.diffName
#a guess string for a word and player
class guess(models.Model):
    user=models.ForeignKey(User, to_field="username",on_delete=models.CASCADE)
    word=models.ForeignKey('word',on_delete=models.CASCADE,null=False)
    guessString=models.CharField(max_length=30)

#The following models are not implemented yet

class stats(models.Model):
    user=models.ForeignKey(User, to_field="username",on_delete=models.CASCADE)
    statDif=models.ForeignKey('difficulty',on_delete=models.CASCADE,null=False)
    totalWords=models.PositiveIntegerField()
    totalCWords=models.PositiveIntegerField()
    corLet=models.PositiveIntegerField()
    wrongLet=models.PositiveIntegerField()

class category(models.Model):
    catName=models.CharField(max_length=30)

class wordBankWord(models.Model):
    cat=models.ManyToManyField(category)
    #ForeignKey('category',on_delete=models.CASCADE,null=False)
    wordName=models.CharField(max_length=200)




