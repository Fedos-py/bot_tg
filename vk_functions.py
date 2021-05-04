import vk_api

LOGIN = '+79679757380'
PASSWORD = 'esteban2012'


def get_friendlist():
    vk_session = vk_api.VkApi(LOGIN, PASSWORD)
    vk_session.auth()
    vk = vk_session.get_api()
    data = vk.friends.getRequests(need_viewed=1)
    return data

def get_suggestionslist():
    vk_session = vk_api.VkApi(LOGIN, PASSWORD)
    vk_session.auth()
    vk = vk_session.get_api()
    data = vk.friends.getSuggestions(filter='mutual')
    return data