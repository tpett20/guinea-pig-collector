from django.shortcuts import render

guinea_pigs = [
  {'name': 'Bernie', 'color': 'brown, white, and black', 'description': 'loves to eat cucumbers', 'age': 5},
  {'name': 'Kodai', 'color': 'tan', 'description': 'loves to popcorn', 'age': 2},
]

# Create your views here.
def about(request):
    return render(request, 'about.html')

def guinea_pigs_index(request):
    return render(request, 'guinea-pigs/index.html', {
        'guinea_pigs': guinea_pigs
    })