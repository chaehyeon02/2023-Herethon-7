from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User

@login_required
def main(request):
    if request.method == 'POST':
        # 여행지 저장
        place = request.POST.get('place')
        user = request.session['user'] # 세션에서 user 가져옴/
        User.objects.filter(userId=user).update(travel_to=place)
        return redirect('match')
    else:
        user_id = request.session['user']
        user = User.objects.get(userId=user_id)
        return render(request, 'main.html', {'user': user})

def match(request):
    return render(request, 'match.html')