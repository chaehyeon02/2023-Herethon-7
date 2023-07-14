from django.shortcuts import render
from account.models import User

def match(request):
    user_id = request.session['user']
    # user_id = 'kim12'
    user = User.objects.get(userId=user_id)

    # 여행지가 같은 사람 중 랜덤으로 뽑기
    random_user = User.objects.exclude(
        userId=user_id
    ).filter(
        travel_to = user.travel_to
    ).order_by('?')[0]

    match_user_info = User.objects.filter(
        userName = random_user
    ).values('userName', 'userType1', 'userType2', 'userType3', 'userType4')
    match_user_name = [user['userName'] for user in match_user_info]
    match_user_type1 = [user['userType1'] for user in match_user_info]
    match_user_type2 = [user['userType2'] for user in match_user_info]
    match_user_type3 = [user['userType3'] for user in match_user_info]
    match_user_type4 = [user['userType4'] for user in match_user_info]
    request.session['match_user'] = match_user_name[0]

    # if match_user_type1[0] == 'option1':
    #     ans1 = '계획형'
    # else:
    #     ans1 = '즉흥형'
    
    # if match_user_type2[0] == 'option3':
    #     ans2 = '바쁘게 움직이는 여행'
    # else:
    #     ans2 = '오직 휴식을 위한 여행'

    # if match_user_type3[0] == 'option1':
    #     ans3 = '사진 찍는 거 좋아요'
    # else:
    #     ans3 = '사진 찍는 거 싫어요'

    # if match_user_type4[0] == 'option1':
    #     ans4 = '번화가'
    # else:
    #     ans4 = '자연, 시골'

    return render(request, 'match_test.html', 
                {
                'user': user, #temp
                'match_user2': match_user_name[0],
                'match_user2_type1': match_user_type1,
                'match_user2_type2': match_user_type2,
                'match_user2_type3': match_user_type3,
                'match_user2_type4': match_user_type4, })

# match_finish
def finish(request):
    # 임시로 user 설정해둠. 나중에 지우기!!
    # request.session['user'] = 'kim'
    user = request.session['user']
    match_user = request.session['match_user']

    user_info = User.objects.filter(
        userId = user
    ).values('travel_to')
    
    user_travel_to = [user['travel_to'] for user in user_info]

    # 매칭된 유저의 정보 받아오기
    match_user_info = User.objects.filter(
        userName = match_user
    ).values('userType1', 'userType2', 'userType3', 'userType4')
    
    match_user_type1 = [user['userType1'] for user in match_user_info]
    match_user_type2 = [user['userType2'] for user in match_user_info]
    match_user_type3 = [user['userType3'] for user in match_user_info]
    match_user_type4 = [user['userType4'] for user in match_user_info]

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

    contents = {
        'user_name': user,
        'user_travel_to': user_travel_to,
        'match_user_name': match_user,
        'ans1': ans1,
        'ans2': ans2,
        'ans3': ans3,
        'ans4': ans4,
    }

    return render(request, 'match_finish_test.html', contents)
