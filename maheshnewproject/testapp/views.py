from django.shortcuts import render

# Create your views here.
def news_info (request):
    return render(request,'testapp/index.html')

def movies_info(request):
    head_msg = 'Movies Information'
    sub_msg1 = 'Eagle Movie was nice.......'
    sub_msg2 = 'OG will come very soon......'
    sub_msg3 = 'Plannong for Aashiqui-3 with  Dinesh & Ganesh.... '
    type ='movies'
    my_dict = {'head_msg' :head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_info(request):
    head_msg = 'Sports Information'
    sub_msg1 = 'Yesterday There Was No Matches...'
    sub_msg2 = 'Upcoming IPL will start Narch-23'
    sub_msg3 = 'Kabaddi Kabaddi'
    type='Sports'
    my_dict = {'head_msg' :head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)


def politics_info(request):
    head_masg = 'Politics Information'
    sub_msg1 = 'Telangana CM Revanth Reddy'
    sub_msg2 = 'Upcoming CM for Ap ???????'
    sub_msg3 = 'If u r not getting Django join the politics.....Become MLA.......'
    type = 'politics'
    my_dict = {'head_msg':head_masg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
