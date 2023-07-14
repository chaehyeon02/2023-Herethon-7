from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User

@login_required
def main(request):
    if request.method == 'POST':
        # 여행지 저장
        place = request.POST.get('place')
        user = request.session.get('user') # 세션에서 user 가져옴
        User.objects.filter(userId=user).update(travel_to=place)
        return render(request, 'match.html', {'user' : user})
    else:
        return render(request, 'main.html')

def match(request):
    return render(request, 'match.html')