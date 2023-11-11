from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ArticleForm
from .models import Article

def articles_view(request):
    # Organiser les articles de plus récente à moins récente
    articles = Article.objects.all().order_by('-date_publication')
    return render(request, 'articles/list.html', context={'articles': articles})

def article_view(request, slug):
    # Utilisation de get_object_or_404 pour éviter une exception inutile
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/detail.html', context={'article': article})

def creer_view(request):
    # Utilisation du nom de la vue dans reverse plutôt que l'URL
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():  # Ajout d'une vérification de validité du formulaire
            form.save()
            return HttpResponseRedirect(reverse('articles:articles'))
    return render(request, 'articles/creer.html', context={'form': form})

#from django.http import HttpResponse
#from django.shortcuts import render
#from django.http import Http404, HttpResponseRedirect
#from django.shortcuts import get_object_or_404
#from django.urls import reverse
#from .db_articles import articles
#from .forms import ArticleForm
#from .models import Article

#def articles_view(request):
    #organiser les articles de plus recente à moins recente
 #   articles = articles = Article.objects.all().order_by('-date_publication')
  #  return render(request,'articles/list.html',context={'articles' : articles})
#https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#def article_view(request,slug):
    #try:
        #article = Article.objects.get(slug=slug)
 #       article =get_object_or_404(Article, slug=slug)
  #      return render(request,'articles/detail.html',context={'article' : article})
    #except Article.DoesNotExist:
        #raise Http404("L'article n'existe pas")

    #return HttpResponse(slug)
    #for article in articles:
        #if article["slug"]==slug:
            #return HttpResponse(article["contenu"])
            #return render(request, 'articles/detail.html',context={'article' : article})
   # return HttpResponse("Aucun article correspondant")
#def creer_view(request):
 #     form = ArticleForm()
  #    if request.method == 'POST':
   #         form = ArticleForm(request.POST, request.FILES)
    #        form.save()
            #return HttpResponseRedirect('/articles/')
     #       return HttpResponseRedirect(reverse('articles:articles'))
      #return render (request,'articles/creer.html', context={'form' : form})  