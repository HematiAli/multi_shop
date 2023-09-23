from random import randint
from uuid import uuid4

import requests
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.views import View

from account.forms import LoginForm, OtpLoginForm, CheckOtpForm
import ghasedakpack

from account.models import Otp, User

SMS = ghasedakpack.Ghasedak('d6efb6c8945a0d8e0c28c7956cf4adb0498eaf42d2b7da1183ba281b00169e5a')


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['phone'], password=data['password'])
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('home:home')

            else:
                form.add_error('phone', 'invalid user data')
        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/login.html', {'form': form})


class OtpLoginView(View):
    def get(self, request):
        form = OtpLoginForm()
        return render(request, 'account/otp_login.html', {'form': form})

    def post(self, request):
        form = OtpLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            code = randint(1000, 9999)
            SMS.verification({'receptor': data["phone"], 'type': '1', 'template': 'randcode', 'param1': code})
            token = str(uuid4())
            Otp.objects.create(phone=data['phone'], code=code, token=token)
            print(code)
            return redirect(reverse('account:check_otp') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/otp_login.html', {'form': form})


class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/check_otp.html', {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if Otp.objects.filter(code=data['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user)
                otp.delete()
                return redirect(reverse('home:home'))
            else:
                form.add_error('phone', 'invalid data')
        return render(request, 'account/check_otp.html', {'form': form})


