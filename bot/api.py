import json
import requests

BASE_URL = 'http://127.0.0.1:8000/api/v1'

def create_user(user_id, user_login, user_name,
                user_last_name, phone_number, subscription, bonus_awarded):
    url = f"{BASE_URL}/bot-users"
    response = requests.get(url=url).text
    data = json.loads(response)
    user_exist = False
    for i in data:
        if i["user_id"] == user_id:
            user_exist = True
            break

    if user_exist == False:
        post = requests.post(url=url, data={'user_id': user_id, 'user_login': user_login,
                                            'user_name': user_name, 'user_last_name': user_last_name,
                                            'phone_number': phone_number, 'subscription': subscription,
                                            'bonus_awarded': bonus_awarded})
        return 'Користувача створено'
    else:
        return 'Користувач існує'
