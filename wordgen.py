
import json
import random
from hangman.models import word, category, wordBankWord
t= open('hangman/words.json')
x=json.load(t)



def randWord(min,max):
    c=0
    rcat=random.choice(category.objects.all())
    while(True):
        c=c+1
        wordBObjs=wordBankWord.objects.filter(cat=rcat)
        rWordObj=random.choice(wordBObjs)
        rword=rWordObj.wordName
        if(len(rword)>=min and len(rword)<=max):
            return([rWordObj,rcat])
        if(c>3000):
            return([rWordObj,rcat])