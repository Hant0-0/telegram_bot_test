from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView

from subscr.models import UserProfule
from subscr.serializers import UserProfileSerializers


class UserProfileAPI(ListCreateAPIView):
    queryset = UserProfule.objects.all()
    serializer_class = UserProfileSerializers


def tel_bot(request):
    return render(request, 'subscr/tel_bot.html')

def user_list(request):
    users = UserProfule.objects.all()
    return render(request, 'subscr/user_list.html', {'users': users})


def check_subscription(request, user_id):
    user = UserProfule.objects.get(user_id=user_id)
    if user.subscription:
        massage = 'Користувач підписаний на канал'
    else:
        massage = 'Користувач не підписаний на канал'
    return JsonResponse({'message': massage})


@csrf_exempt
def send_message(request, user_id):
    try:
        user_id = int(user_id)
        text = request.POST.get('message', '')

        # Тут можна додати логіку, пов'язану з обробкою повідомлення, якщо вона необхідна

        message = 'Повідомлення надіслано користувачу.'
        return JsonResponse({'message': message})
    except Exception as e:
        response_data = {'message': f'Помилка: {str(e)}'}
        return JsonResponse(response_data, status=500)

@csrf_exempt
def set_mark(request, user_id, mark):
    user = UserProfule.objects.get(user_id=user_id)
    user.mark = mark
    user.save()
    message = f"Відмітка {mark} встановлена для користувача"
    return JsonResponse({'message': message})

