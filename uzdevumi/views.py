from django.shortcuts import render
from django.http import HttpResponse
from .forms import (
    UserForm,
    UserNameForm,
    UploadCsvForm,
)

from .models import User

from .csv_handler import (
    read_and_decode_csv,
    lietotaji_csv_rows_to_db,
)

def meklet_lietotaju(request):

    form = UserNameForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user_name = form.cleaned_data['user_name']
            lietotaji = User.objects.filter(lietotajs=user_name)

            context = {
                'lietotaji': lietotaji,
            }

            return render(
                request,
                template_name='lietotaji.html',
                context=context,
            )

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='user.html',
        context=context,
    )



def visi_lietotaji(request):

    lietotaji = User.objects.all()

    context = {
        'lietotaji': lietotaji,
    }

    return render(
        request,
        template_name='lietotaji.html',
        context=context,
    )


def viens_lietotajs(request, user_id):

    user = User.objects.get(id=user_id)

    context = {
        'user': user,
    }

    return render(
        request,
        template_name='lietotajs.html',
        context=context,
    )


def pievienot_lietotaju(request):

    form = UserForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            user = form.save()

            context = {
                'user': user,
            }

            return render(
                request,
                template_name='lietotajs.html',
                context=context,
            )

    return render(
        request,
        template_name='user.html',
        context={'form': form}
    )

def upload_csv_to_db(request):

    form = UploadCsvForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':

        if form.is_valid():

            decoded_csv = read_and_decode_csv(request.FILES['csv_file'])
            lietotaji_csv_rows_to_db(decoded_csv)

            return HttpResponse('OK')

    context = {
        'form': form,
    }

    return render(
        request,
        template_name='user.html',
        context=context,
    )