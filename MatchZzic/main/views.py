from django.shortcuts import redirect, render
from .models import Post
from account.models import User
from .forms import PostForm

def main(request):
    # 해당 user에 여행지 저장
    # user_id = request.session.get('user')
    # user = User.objects.get(userId=user_id)
    
    # 여행지 저장
    if request.method == 'POST':
        place = PostForm(request.POST)
        if place.is_valid():
            data = place.save(commit=False)
            #data.user = user
            data.place = request.POST.get('placeName')
            data.save()
            return redirect('main')
    else:
        place = PostForm()
    return render(request, 'main.html', {'place':place})


def match(request):
    return render(request, 'match.html')