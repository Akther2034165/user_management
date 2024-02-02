from django.shortcuts import render
from . models import ContactModel
# Create your views here.
def index(request):
    users = ContactModel.objects.all()
    context = {
        'users': users
    }
    return render(request, 'um_app/user.html', context)