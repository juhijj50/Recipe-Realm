from django.shortcuts import render, redirect
from .models import Receipe
from django.http import HttpResponse

# Create your views here.
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')  # This will fetch the uploaded file

        # Only create the recipe if all fields are provided
        if receipe_name and receipe_description and receipe_image:
            Receipe.objects.create(
                receipe_image=receipe_image,
                receipe_name=receipe_name,
                receipe_description=receipe_description
            )
        else:
            # Optionally, you could return an error message if form validation fails
            print("All fields are required")

        return redirect('recepies')

    queryset = Receipe.objects.all()
    
    if request.GET.get('search'):
       queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    context = {'receipes': queryset}

    return render(request, 'recepies.html', context)

def update_receipe(request, id):
    receipe = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description

        if receipe_image:
            receipe.receipe_image = receipe_image

        receipe.save()
        return redirect('recepies')

    context = {'receipe': receipe}
    return render(request, 'update_receipes.html', context)

def delete_receipe(request, id):
    receipe = Receipe.objects.get(id=id)  # This will return a 404 if not found
    receipe.delete()
    return redirect('recepies')
