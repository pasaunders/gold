from django.shortcuts import render, redirect
from random import randint


def index(request):
    if 'activities' in request.session:
        context = {
            'total': request.session['total'],
            'activities': reversed(request.session['activities'])
        }
    else:
        context = {}
    return render(request, 'get_gold/index.html', context)


def process(request):
    locations = {
        'farm': randint(10, 20),
        'cave': randint(5, 10),
        'house': randint(2, 5),
        'casino': randint(-50, 50),
    }
    if 'total' not in request.session:
        request.session['total'] = 0
        request.session['activities'] = []
    if request.method == 'POST':
        activity = "You visited the {} and made {} gold.".format(
            request.POST['building'], locations[request.POST['building']]
            )
        import pdb; pdb.set_trace()
        request.session['activities'].append(activity)
        new_active = request.session['activities']
        request.session['activities'] = new_active
        request.session['total'] += locations[request.POST['building']]
    return redirect('/')
