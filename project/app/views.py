from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

from .forms import UpdateForm
from .models import Contactus, Feedback, UrlDatabase
from .random_forest import noa

global url


def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about-us.html')


def services(request):
    return render(request, 'services.html')


def login(request):
    return render(request, 'login.html')


def contact(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        comments = request.POST['comments']
        contactus = Contactus(first_name=first_name, last_name=last_name, email=email, phone=phone, comments=comments)
        contactus.save()
        return redirect('/')
    return render(request, 'contact.html')


def admin(request):
    """"e0d123e5f316bef78bfdf5a008837577"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        security = request.POST["secuirty"]
        if security == "e0d123e5f316bef78bfdf5a008837577":
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('adminui')
            else:
                messages.info(request, "Invalid Info")
                return redirect('admin')
        else:
            messages.info(request, "Invalid Info")
            return redirect('admin')

    else:
        return render(request, "admin_login.html")


def newuser(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User Name Taken")
                return redirect('newuser')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('newuser')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password1, email=email)
                user.save()
                return redirect('existinguser')
        else:
            messages.info(request, "Password Not Matching")
            return redirect('newuser')


    else:
        return render(request, 'new_user_login.html')
    return redirect('/')


def existinguser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('userui')
        else:
            messages.info(request, "Invalid Info")
            return redirect('existinguser')

    else:
        return render(request, "existing_user_login.html")


# after user login part
def userui(request):
    return render(request, 'user_ui.html')


def website_checking(request):
    if request.method == "POST":
        url = request.POST['url']
        result = noa(url)
        ud = UrlDatabase(user=request.user, link=url, status=result)
        ud.save()
        if result == 1:
            return render(request, 'legit.html', {'url': url})
        else:
            return render(request, 'phis.html', {'url': url})
    else:
        return render(request, 'u_check.html')


def feedback(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        comments = request.POST['comments']
        feedback = Feedback(username=username, email=email, phone=phone, comments=comments)
        feedback.save()
        return redirect('userui')
    return render(request, 'u_feedback.html')


def ulogout(request):
    auth.logout(request)
    return redirect('/')


# after admin login part
def adminui(request):
    return render(request, 'admin_ui.html')


def url_database(request):
    uds = reversed(UrlDatabase.objects.all())
    return render(request, 'a_url_database.html', {'uds': uds})


def feedback_database(request):
    feedbacks = reversed(Feedback.objects.all())
    return render(request, 'a_feedback_database.html', {'feedbacks': feedbacks})


def delete_url_database(request, id):
    if request.method == "POST":
        ud = UrlDatabase.objects.get(pk=id)
        ud.delete()
        return redirect('url_database')


def alogout(request):
    auth.logout(request)
    return redirect('/')


def update_url_database(request, id):
    if request.method == 'POST':
        ud = UrlDatabase.objects.get(pk=id)
        form = UpdateForm(request.POST, instance=ud)
        if form.is_valid():
            form.save()
        return redirect('url_database')
    else:
        ud = UrlDatabase.objects.get(pk=id)
        form = UpdateForm(instance=ud)
        return render(request, 'update_url_database.html', {'form': form})


def error_404_handler(request, exception):
    return render(request, 'error.html')
