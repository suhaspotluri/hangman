import json
from hangman.models import wordBankWord, category
t= open('hangman/dataClean.json')
x=json.load(t)
def dol():
    for i in x:
        catObj=category(catName=i)
        catObj.save()
        for z in x[i]:
            wordObj=wordBankWord(wordName=z)
            wordObj.save()
            wordObj.cat.add(catObj)
            wordObj.save()
            print("Inserted "+z+" cat "+catObj.catName)
    return "Done"
