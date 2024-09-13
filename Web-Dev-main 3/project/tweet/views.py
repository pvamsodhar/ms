from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def tweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'tweets' : tweets})

@login_required 
def tweetCreate(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('index')
    else:
        form = TweetForm()
    return render(request, 'tweetForm.html', {'form' : form})

@login_required
def tweetEdit(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.user != tweet.user:
        return redirect('index')
    
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweetForm.html', {'form': form})

@login_required
def tweetDelete(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    if request.user == tweet.user:
        tweet.delete()
    return redirect('index')

def search(request):
    query = request.GET.get('q')
    context = request.GET.get('context')

    if context == 'home':
        results = search_homepage_content(query)
    elif context == 'tweets':
        results = Tweet.objects.filter(text__icontains=query)
    else:
        results = []

    return render(request, 'searchResults.html', {'results': results, 'query': query, 'context': context})

def search_homepage_content(query):
    sections = [
        {'title': 'Tweet Section', 'content': 'Click below to view and create tweets.'},
        {'title': 'Upcoming Features', 'content': 'Stay tuned for more features like Discord-like server rooms, games like GeoGuessr, quizzes, etc.'}
    ]
    results = [section for section in sections if query.lower() in section['title'].lower() or query.lower() in section['content'].lower()]
    return results

