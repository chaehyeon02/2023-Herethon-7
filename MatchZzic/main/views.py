from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User

@login_required
def main(request):
    if request.method == 'POST':
        # 여행지 저장
        place = request.POST.get('place', None)
        temp_user_id = request.session.get('temp_user_id')  # 세션에서 temp_user_id 가져옴
        post = User(travel_to=place, userId=temp_user_id)
        post.save()
        return redirect('match')
    else:
        return render(request, 'main.html')

def match(request):
    return render(request, 'match.html')