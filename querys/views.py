# def index(request):
from django.shortcuts import render
from .forms import RestaurantForm

    # john = Author.objects.create(name="John")
    # paul = Author.objects.create(name="Paul")
    # george = Author.objects.create(name="George")
    # ringo = Author.objects.create(name="Ringo")
    # entry = Author.objects.filter(name="John")


    # return render(request, "index.html", {'entry': entry})


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            return render(request, 'index.html', {'form': form})
    context = {'form': RestaurantForm()}
    return render(request, 'index.html', context)