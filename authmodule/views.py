from django.shortcuts import render
from .forms import * 
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
import random
import json
# Create your views here.
def signup_screen(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            return HttpResponse('Register Successful')
        
    else :
        form = SignupForm()
    return render(request,'signup.html',context={"form" : form})


def login_screen(request):    
    return render(request,'login.html')

def sending_mail_for_otp(request,user_email):
    if request.method == 'POST':    
        verfication_otp = random.randint(1000,9999)
        request.session['otp'] = verfication_otp
        send_mail(
            "Django Mail",
            f"This is the otp : {verfication_otp}",
            'postmaster@sandboxeec3e874afe1487c8873e2df11cea743.mailgun.org',
            [user_email],
            fail_silently=False,
            )
        print('login_email_send')
        return JsonResponse({'status' : 'Correct Method'})
    else : 
        return JsonResponse({'status' : 'Wrong Method'})

    

def verifyOtp(request):
    data = request.body
    user_otp = ''.join(json.loads(data)['otp_list'])
    gen_otp = request.session.get('otp')
    print(user_otp)
    print(gen_otp)
    if(str(user_otp) == str(gen_otp)):
       return JsonResponse({'status' : 'Successful'}) 
    else : 
       return JsonResponse({'status' : 'Failed'})
         
