from django.shortcuts import render
from utils.get_current_site_from_env import get_current_site_from_env
from utils.token_generator import TokenGenerator, account_activation_token
from accounts.forms import SignupForm
from utils.mailer import Mailer
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from utils.utils import render_message
from utils.login_decorators import team_user_required


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data.get('email')
            if not to_email.endswith('@iitrpr.ac.in'):
                return render_message(request, 'Access Denied', 'Sorry ... only IIT Ropar domain emails can be used to sign up!')
            mailer = Mailer()
            user = form.save(commit=False)
            user.is_active = False
            user.username = to_email
            try:
                user.save()
                current_site = get_current_site_from_env()
                message = render_to_string('accounts/activate_account_email.html', {
                    'user': user,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                response = mailer._send_email(
                    to_email, 'CDCRC User Registration Activation', message)
                print("Mail Response: ", response)
                if(response == 'fail'):
                    raise Exception('Mail Service is down! 😢')

                return render_message(request,
                                      'Email Confirmation',
                                      'Thank you for joining CDCRC Internal Network. We have sent an activation link to your email. Once verified, you can access plethora of resources on the webpage. Hope to see you onboard soon!'
                                      )
            except Exception as e:
                # Deleting the user
                if user.id != None:
                    print("Deleting user: ", user.id)
                    user.delete()

                return render_message(request,
                                      'An error occurred while creating your account',
                                      'Trace: ' + str(e)
                                      )

    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        t = urlsafe_base64_decode(uidb64)
        uid = force_text(t)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None
        return render_message(request,
                              'Error in activating the account',
                              'Trace: '+str(e),
                              )
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render_message(request,
                              'Account Activated',
                              'Congratulations, your account was successfully activated!'
                              )
    else:
        return render_message(request,
                              'Invalid Activation Link',
                              'The activation link is invalid!'
                              )


def check_account_status(request):
    message = str(request.user.get_user_name()) + " " + str(request.user.is_team_member()
                                                            ) + " " + str(request.user.student_profile_completed())
    return render_message(request, 'User Status', message)
