
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login, logout
from school_users.forms import UserLoginForm, RegisterForm, AdmisssionForm
from copy import deepcopy
from school_users.models import MyUsers
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        # refer_url = request.META['HTTP_REFERER']
        userlogin = UserLoginForm(request.POST)
        if not userlogin.is_valid():
            return HttpResponse('无效')
        data = userlogin.cleaned_data
        try:
            user = MyUsers.objects.filter(username=data['name'])[0]
        except Exception:
            return HttpResponse('用户不存在!')
        encode_pwd = user.password
        is_true = False
        if check_password(data['password'], encode_pwd):
            is_true = True
        if is_true:
            login(request, user)
            # return HttpRespone('用户登录成功')
            return redirect('Index')
        else:
            return HttpResponse('密码错误')


def user_logout(request):
    refer_url = request.META['HTTP_REFERER']
    logout(request)
    return redirect(refer_url)


def user_register(request):
    form = RegisterForm(request.POST)
    if not form.is_valid():
        return HttpResponse("请检查提交的参数")
    form.instance.password = make_password(form.instance.password)
    user = form.save()
    login(request, user)
    # return HttpRespone('用户登录成功')
    refer_url = request.META['HTTP_REFERER']
    return redirect(refer_url)


def user_admission(request):
    # refer_url = request.META['HTTP_REFERER']
    # data = deepcopy(request.POST)

    res_data = AdmisssionForm(request.POST)
    print(res_data)
    if not res_data.is_valid():
        return HttpResponse('请检查提交参数')
    res_data.save()
    return HttpResponse('提交成功')
