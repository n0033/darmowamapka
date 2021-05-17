from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic import View
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import (
    Text,
    User,
    Mail,
    Style
)
from .forms import UserForm


def get_style():
    style = Style.objects.filter(currently_used=True)
    if style.count() == 1:
        return style[0]
    else:
        return None


def send_mail(receiver):
    mail = Mail.objects.get(name='default_mail')
    email = EmailMessage(
        mail.title,
        mail.content,
        'mapka@darmowamapka.pl',
        [receiver]
    )
    email.attach_file(mail.attachment.path)
    return email.send()


class MainView(View):
    def get(self, *args, **kwargs):
        context = {
            'title': Text.objects.get(title="title"),
            'submit_button': Text.objects.get(title='submit_button'),
            'form_title_1': Text.objects.get(title='form_title_1'),
            'form_title_2': Text.objects.get(title='form_title_2'),
            'form_title_3': Text.objects.get(title='form_title_3'),
            'form_title_4': Text.objects.get(title='form_title_4'),
            'form_subtitle_4': Text.objects.get(title='form_subtitle_4'),
            'main_page_card_title': Text.objects.get(title='main_page_card_title'),
            'footer_1': Text.objects.get(title='footer_1'),
            'checkbox_label': Text.objects.get(title='checkbox_label'),
            'style': get_style(),
        }
        return render(self.request, 'main.html', context)

    def post(self, *args, **kwargs):
        form = UserForm(self.request.POST or None)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            checkbox_checked = form.cleaned_data.get('checkbox')
            user = User(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
                checkbox_checked=checkbox_checked,
                cookie_id=self.request.COOKIES.get('session')
            )
            user.save()
            return redirect('main:clip')
        else:
            messages.info(self.request, 'Sprawdź poprawność wprowadzonych danych')
            return redirect('main:main')


def clip(request):
    context = {
        'clip_page_title': Text.objects.get(title='clip_page_title'),
        'video_url': Text.objects.get(title='video_url'),
        'clip_page_card_title': Text.objects.get(title='clip_page_card_title'),
        'footer_1': Text.objects.get(title='footer_1'),
        'style': get_style(),
    }
    try:
        User.objects.get(cookie_id=request.COOKIES.get('session'))
        return render(request, 'clip.html', context)
    except ObjectDoesNotExist:
        return redirect("main:main")
    except MultipleObjectsReturned:
        users = User.objects.filter(cookie_id=request.COOKIES['session'])
        # delete duplicate user objects
        users = users[:len(users) - 1]
        for user_object in users:
            user_object.delete()
        return render(request, 'clip.html', context)


@csrf_exempt
def video_watched(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(cookie_id=request.COOKIES.get('session'))
            user.video_watched = True
            user.save()
            return HttpResponse("OK")
        except ObjectDoesNotExist:
            return redirect("main:main")
        except MultipleObjectsReturned:
            users = User.objects.filter(cookie_id=request.COOKIES['session'])
            user = users[len(users) - 1]
            # delete duplicate user objects
            users = users[:len(users) - 1]
            for user_object in users:
                user_object.delete()
            if user.video_watched:
                user.video_watched = True
                user.save()
                return HttpResponse("OK")
            else:
                return redirect("main:main")
    else:
        return redirect("main:main")


def ebook_sent(request):
    context = {
        'ebook_sent_title': Text.objects.get(title='ebook_sent_title'),
        'ebook_sent_1': Text.objects.get(title='ebook_sent_1'),
        'ebook_sent_button': Text.objects.get(title='ebook_sent_button'),
        'ebook_sent_card_title': Text.objects.get(title='ebook_sent_card_title'),
        'footer_1': Text.objects.get(title='footer_1'),
        'style': get_style(),
    }
    try:
        user = User.objects.get(cookie_id=request.COOKIES.get('session'))
        if user.video_watched:
            send_mail(user.email)
            user.ebook_sent = True
            response = render(request, "ebook_sent.html", context)
            response.delete_cookie('session')
            return response
        else:
            return redirect("main:main")
    except ObjectDoesNotExist:
        return redirect("main:main")
    except MultipleObjectsReturned:
        users = User.objects.filter(cookie_id=request.COOKIES['session'])
        user = users[len(users) - 1]
        # delete duplicate user objects
        users = users[:len(users) - 1]
        for user_object in users:
            user_object.delete()
        if user.video_watched:
            send_mail(user.email)
            user.ebook_sent = True
            response = render(request, "ebook_sent.html", context)
            response.delete_cookie('session')
            return response
        else:
            return redirect("main:main")
