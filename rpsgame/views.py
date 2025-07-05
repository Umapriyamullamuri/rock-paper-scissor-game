from django.shortcuts import render
from numpy import random
# Create your views here.
def home(request):
    choices=['ROCK','PAPER','SCISSOR']
    result=None
    person=''
    computer=''
    if request.method == 'POST' :
        person=request.POST.get('selectedValue')
        computer=random.choice(choices)
        if person=='ROCK':
            if computer=='ROCK':
                result='DRAW'
            elif computer=='PAPER':
                result='LOOSE'
            elif computer=='SCISSOR':
                result='WIN'
        if person=='PAPER':
            if computer=='ROCK':
                result='WIN'
            elif computer=='PAPER':
                result='DRAW'
            elif computer=='SCISSOR':
                result='LOOSE'
        if person=='SCISSOR':
            if computer=='ROCK':
                result='LOOSE'
            elif computer=='PAPER':
                result='WIN'
            elif computer=='SCISSOR':
                result='DRAW'
    return render(request, 'home.html', {
        'result' : result,
        'person' : person,
        'computer': computer
    })
