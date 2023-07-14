from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post,User
from .forms import PostForm

@login_required
def main(request):
    if request.method == 'POST':
        place = request.POST['place']
        post = Post(travel_to=place, user=request.user)
        
        # 동일한 여행지 필터링
        Post.objects.filter(place__exact=request.POST.get('place'))
        post.save()
        return redirect('match')
    else:
        form = PostForm()
    return render(request, 'main.html', {'form': form})

def match(request):
    return render(request, 'match.html')