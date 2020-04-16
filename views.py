from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hangman.models import difficulty, word, guess, wordBankWord, stats
import hangman.wordgen


class MainView(LoginRequiredMixin, View) :
    def get(self, request):
        dif = difficulty.objects.all();
        uname=request.user.username
        ctx = {'difficulty_list':dif,'user':uname};

        return render(request, 'hangman/dif_list.html', ctx)


class GameView(LoginRequiredMixin, View):
    def get(self, request,pk,wid,wk):
        alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
        cl=""
        wl=""
        x="123456789012345678901234567890"


        if(pk != 0):
            #if(len(word.objects.filter(user=request.user))!=0):
             #   wordObj=word.objects.filter(user=request.user)[0]
              #  ctx={'wordLen':wordObj.wordLen,'wk':wk,'alph':alph,'cl':cl,'wl':wl,'wordObj':wordObj.id,'word':wordObj.wordName}
               # return render(request, 'hangman/game.html', ctx)
            difOb=difficulty.objects.filter(id=pk)[0]
            min=difOb.wordLenMin
            max=difOb.wordLenMax
            wList=hangman.wordgen.randWord(min,max)
            w=wList[0].wordName
            catObj=wList[1]
            cat=catObj.catName
            wLen=x[:len(w)]
            wordObj=word(wordName=w,wordDif=difOb,wordLen=len(w),user=request.user)
            wordObj.save()
            #ctx={'wordLen':wLen,'wk':wk,'alph':alph,'cl':cl,'wl':wl,'wordObj':wordObj.id}
        else:
            glist=guess.objects.filter(word=wid)
            if(len(glist)==0):

                wordObj=word.objects.filter(id=wid)[0]
                gObj=guess(guessString=wk,word=wordObj,user=request.user)
                gObj.save()
            else:
                gObj=glist[0]
                if wk not in gObj.guessString:
                    gObj.guessString=gObj.guessString+wk
                    gObj.save()

            wordObj=word.objects.filter(id=wid)[0]
            wL=wordObj.wordLen
            wLen=x[:wL]
            for letter in (gObj.guessString):
                if letter in wordObj.wordName.lower():
                    if letter not in cl:
                        c=wordObj.wordName.lower().count(letter)
                        for times in range(c):
                            cl=cl+letter
                else:
                    if letter not in wl:
                        wl=wl+letter
        cat=wordBankWord.objects.filter(wordName=wordObj.wordName)[0].cat.all()[0].catName
        if(len(wl)>=5):

            ctx={'word':wordObj.wordName,'win':False,'attempts':len(wl)+len(cl),'corNum':len(cl)}
            wordObj.delete()
            statUpdate(cl,wl,1,wordObj,request)
            return render(request, 'hangman/lost.html', ctx)
        elif(len(cl)==wordObj.wordLen):
            ctx={'word':wordObj.wordName,'win':True,'wrongNum':len(wl),'corNum':len(cl)}
            statUpdate(cl,wl,2,wordObj,request)
            wordObj.delete()
            return render(request, 'hangman/lost.html', ctx)
        else:
            ctx={'wordLen':wLen,'wk':wk,'alph':alph,'cl':cl,'wl':wl,'wordObj':wordObj.id,'word':wordObj.wordName,'cat':cat}
            return render(request, 'hangman/game.html', ctx)
def statUpdate(cl,wl,over,wordObj,request):
    res=stats.objects.filter(user=request.user).filter(statDif=wordObj.wordDif)
    if len(res)==0:
        statObj=stats(user=request.user,statDif=wordObj.wordDif,totalWords=0,totalCWords=0,corLet=0,wrongLet=0)
        statObj.save()
    else:
        statObj=res[0]
        #Wrong, loss
    if over==1:
        statObj.totalWords=statObj.totalWords+1
        statObj.corLet=statObj.corLet+len(cl)
        statObj.wrongLet=statObj.wrongLet+len(wl)
        #win
    elif over==2:
        statObj.totalWords=statObj.totalWords+1
        statObj.corLet=statObj.corLet+len(cl)
        statObj.wrongLet=statObj.wrongLet+len(wl)
        statObj.totalCWords=statObj.totalCWords+1
    statObj.save()


class LostView(LoginRequiredMixin, View):
    def get(self, request):
        ctx={'hi':'hi'}

        return render(request, 'hangman/lost.html', ctx)
class ScoreboardView(LoginRequiredMixin,View):
    def get(self,request):
        dif=difficulty.objects.all()
        dif1=stats.objects.filter(statDif=dif[0]).order_by('-totalCWords')
        dif2=stats.objects.filter(statDif=dif[1]).order_by('-totalCWords')
        dif3=stats.objects.filter(statDif=dif[2]).order_by('-totalCWords')

        ctx={'dif1':dif1,'dif2':dif2,'dif3':dif3}
        return render(request, 'hangman/scoreboard.html',ctx)



def logout_request(request):
    auth.logout(request)
    messages.info(request, "Logged out!")
    return redirect("main:homepage")
