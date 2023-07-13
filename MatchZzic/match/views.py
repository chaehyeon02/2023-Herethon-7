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

    return render(request, 'match_test.html', {'match_user': match_user, 'match_user_name': match_user_name[0], 'match_user_type1': match_user_type1[0], 'match_user_type2': match_user_type2[0], 'match_user_type3': match_user_type3[0], 'match_user_type4': match_user_type4[0]})

# match_finish
def finish(request):
    match_user = request.GET.getlist('match_user')
    # select_user = MatchUser.objects.filter(
    #     userName=matching_user
    # )
    # match_user_name = [user['userName'] for user in match_user]
    match_user_name = [user['userName'] for user in match_user]

    return render(request, 'match_finish_test.html', {'match_user': match_user_name})

    # return render(request, 'match_finish_test.html', {'match_user': match_user_name})
