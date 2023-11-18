from django.shortcuts import render
from django.http import HttpResponse


from django.template import RequestContext
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse

""" from .models import Sound
from .form import SoundForm

def contact(request):
    # Handle file upload
    if request.method == 'POST':
        form = SoundForm(request.POST, request.FILES)
        if form.is_valid():
            newsound = Sound(docfile = request.FILES['soundfile'])
            newsound.save()

            # Redirect to the document list after POST
            return render(request, 'reader/reader.html', {'sound': newsound})
    else:
        form = SoundForm() # A empty, unbound form

    # Render list page with the documents and the form
    return render(request, 'reader/reader.html') """




# Create your views here.

def contact(request):
    pass

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             message = form.cleaned_data['message']
#             print(message)
#             return render(request, 'reader/reader.html', {'message': message})

#     form = ContactForm()
#     return render(request, 'reader/reader.html', {'form': form})