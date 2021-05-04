import vk_api


LOGIN = '+79679757380'
PASSWORD = 'esteban2012'
myid = 235573478

vk_session = vk_api.VkApi(LOGIN, PASSWORD)
vk_session.auth()
vk = vk_session.get_api()

data = vk.friends.getSuggestions(filter='mutual', count=500)['items']
print(data)

for elem in data:
    print(vk.friends.add(user_id=elem['id']))