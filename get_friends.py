import vk_api


LOGIN = '+79679757380'
PASSWORD = 'esteban2012'
myid = 235573478

vk_session = vk_api.VkApi(LOGIN, PASSWORD)
vk_session.auth()
vk = vk_session.get_api()

data = vk.friends.getRequests(need_viewed=1)
items = data['items']
print(data)
print(items)

for elem in items:
    try:
        mutual = vk.friends.getMutual(target_uid=elem)
        if len(mutual) >= 400:
            print(True)
            vk.friends.add(user_id=elem)
            info = vk.users.get(user_ids=elem)[0]
            print(f'Одобрили заявку в друзья от {info["first_name"]} {info["last_name"]} id={info["id"]}')
    except Exception as e:
        print(e)