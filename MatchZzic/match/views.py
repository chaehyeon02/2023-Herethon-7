from django.shortcuts import render
from .models import MatchUser
import json

from account.models import User

def match(request):
    # user_id = request.session.get('user')
    user_id = 'kim12'
    user = User.objects.get(userId=user_id)

    # 로그인한 사용자의 userType 값 가져오기
    user_types = [
        user.userType1,
        user.userType2,
        user.userType3,
        user.userType4,
    ]

    # match_user에 userType1, userType2, userType3, userType4가 현재 로그인한 사용자와 일치하는 행 찾기
    match_user = User.objects.exclude(
        userId=user_id
    ).filter(
        userType1__in=user_types,
        userType2__in=user_types,
        userType3__in=user_types,
        userType4__in=user_types,
    ).values('userName', 'userType1', 'userType2', 'userType3', 'userType4')
        
    match_user_name = [user['userName'] for user in match_user]
    match_user_type1 = [user['userType1'] for user in match_user]
    match_user_type2 = [user['userType2'] for user in match_user]
    match_user_type3 = [user['userType3'] for user in match_user]
    match_user_type4 = [user['userType4'] for user in match_user]

    if match_user_type1[0] == 'option1':
        ans1 = '계획형'
    else:
        ans1 = '즉흥형'
    
    if match_user_type2[0] == 'option3':
        ans2 = '바쁘게 움직이는 여행'
    else:
        ans2 = '오직 휴식을 위한 여행'

    if match_user_type3[0] == 'option1':
        ans3 = '사진 찍는 거 좋아요'
    else:
        ans3 = '사진 찍는 거 싫어요'

    if match_user_type4[0] == 'option1':
        ans4 = '번화가'
    else:
        ans4 = '자연, 시골'

    request.session['match_user_name'] = match_user_name[0]
    return render(request, 'match.html', 
                {'match_user_name': match_user_name[0], 'ans1': ans1, 'ans2': ans2, 'ans3': ans3, 'ans4': ans4 })

# match_finish
def finish(request):
    # 임시로 user 설정해둠. 나중에 지우기!!
    request.session['user'] = 'kim'
    user = request.session['user']
    match_user = request.session['match_user_name']

    match_user_travel = User.objects.filter(
        userName = user
    ).values('travel_to')

    

    contents = {
        'user_name': user,
        'match_user_travel': match_user_travel,
    }

    return render(request, 'match_finish_test.html', contents)
