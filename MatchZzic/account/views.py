from django.shortcuts import render, redirect, get_object_or_404
from .models import User, TempUser
from .forms import UserForm, TempUserForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def first(request):
    return render(request, 'start.html')

def signup(request):
    if request.method == "POST":
        form = TempUserForm(request.POST)
        if form.is_valid():
            temp_user = form.save()  # 폼을 저장하고 TempUser 객체를 받아옵니다.
            request.session['temp_user_id'] = temp_user.id
            return redirect(reverse('signup2', kwargs={'temp_user_id': temp_user.id}))
    else:
        form = TempUserForm()
    return render(request, 'signup_popup.html', {'form': form})

def signup2(request, temp_user_id):
    temp_user_id = request.session.get('temp_user_id')  # 세션에서 temp_user_id 가져옴
    temp_user = get_object_or_404(TempUser, id=temp_user_id)
    
    if request.method == "POST":
        user_form = UserForm()
        if temp_user.userRrn2 == '2' or temp_user.userRrn2 == '4':
            user = user_form.save(commit=False)
            user.userName = temp_user.userName
            user.userId = temp_user.userId
            user.userPwd = temp_user.userPwd
            user.userRrn1 = temp_user.userRrn1
            user.userRrn2 = temp_user.userRrn2
            user.userLink = temp_user.userLink
            user.userType1 = request.POST.get('userType1', '')
            user.userType2 = request.POST.get('userType2', '')
            user.userType3 = request.POST.get('userType3', '')
            user.userType4 = request.POST.get('userType4', '')
            user.save()
            login(request)
            return redirect('login')
    else:
        user_form = UserForm(initial={
            'userName': temp_user.userName,
            'userId': temp_user.userId,
            'userPwd': temp_user.userPwd,
            'userRrn1': temp_user.userRrn1,
            'userRrn2': temp_user.userRrn2,
            'userLink': temp_user.userLink
        })
    return render(request, 'selectType_popup.html', {'user_form': user_form})


def login(request):
    response_data = {}
    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('userId', None)
        login_password = request.POST.get('userPwd', None)


        if not (login_username and login_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            myuser = User.objects.get(userId=login_username) 
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if (login_password == myuser.userPwd):
                request.session['user'] = myuser.userId
                return redirect('main_app:main')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'login.html',response_data)

@login_required
def mypage(request):
    user_instance = request.user
    
    context = {
        'user_instance': user_instance
    }

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user_instance)
        if form.is_valid():
            form.save()
            return render(request, 'mypage.html', context)
    else:
        form = UserForm(instance=user_instance)
    
    return render(request, 'mypage.html', {'form': form})