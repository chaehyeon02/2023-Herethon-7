from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User

@login_required
def main(request):
    if request.method == 'POST':
        place = request.POST['place']
        post = User(travel_to=place, user=request.user)
        
        # 동일한 여행지 필터링
        User.objects.filter(place__exact=request.POST.get('place'))
        post.save()
        return redirect('match')
    else:
        return render(request, 'main.html')

def match(request):
    return render(request, 'match.html')