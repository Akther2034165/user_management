from django.shortcuts import render
from um_app.forms import ContactForm
import datetime
import requests

# Create your views here.
def home(request):
    current_datetime = datetime.datetime.now()
    quotable_api_url = "https://api.quotable.io/random"
    response = requests.get(quotable_api_url)

    if response.status_code == 200:
        quote_data = response.json()
        random_quote = quote_data.get('content', 'No quote available')
        quote_author = quote_data.get('author', 'Unknown Author')
    else:
        random_quote = 'Failed to fetch quote'
        quote_author = 'Unknown Author'
        
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
             form.save()
        form = ContactForm()
    else:
        form = ContactForm()
    
    context = {
        'form' : form,
        'current_datetime' : current_datetime,
        'random_quote': random_quote,
        'quote_author': quote_author,
    }
    return render(request, 'home.html', context)