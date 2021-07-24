from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    # return  HttpResponse('SADIA')
    return render(request, 'home.html',{'hithere':'this is sadia'})

# def eggs(request):
#     return  HttpResponse('EEGS are great')
def count(request):
    fulltext= request.GET['fulltext']
    wordlist= fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
        # increase
            worddictionary[word]+=1
        else:
            # Add
            worddictionary[word]=1
    sortedWords=sorted(worddictionary.items(),key= operator.itemgetter(1),reverse=True)
    # return render(request, 'count.html')
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortedWords':sortedWords})
def about(request):
    # return  HttpResponse('SADIA')
    return render(request, 'about.html')
