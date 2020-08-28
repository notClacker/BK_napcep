import vk
import time
from tokens import me_user_token
from tokens import me_service_token


# you can processing the mans as you wants here
def man_processing(man):
    result = ""
    result += man['first_name'] + ' '
    result += man['last_name'] + ' '
    if man.get('city'):
        result += '| City: ' + man.get('city').get('title') + ' '
    result += '\n'
    print(result)

    output_file = 'users.txt'
    with open(output_file, 'a+') as file:
        file.write(result)

def get_ids_from_chat(input_chat_id):
    ids = []
    response = api.messages.getChat(chat_id=input_chat_id)
    for i in response:
        print(i, ': ',response[i])
    for id in response['users']:
        ids.append(id)
        # print(id, ' ', end = '')
    return ids

def get_wrong_ids(ids):
    wrong_ids = []
    for id in ids:
        print("ID : ", id)
        last_worked_time = time.time()
        last_not_worked_time = time.time()
        try:
            response = api.users.get(user_ids=id, fields='city')
            if (len(response) > 0):
                man_processing(response[0])

        except vk.exceptions.VkAPIError:
            time.sleep(0.1)
            wrong_ids.append(id)
    return wrong_ids


# Set your user_token here
user_token = me_user_token

session = vk.Session(access_token=user_token)
api = vk.API(session, v=5.112)

# Test for working of the session
response = api.users.get(user_ids=1, fields='city')
print(response[0])

# Set the chat id here
chat_id = 1
ids = get_ids_from_chat(chat_id)

wrong_ids = []
wrong_ids = get_wrong_ids(ids)

# Rescanning the wrong ids
if (len(wrong_ids) > 0):
    count = len(wrong_ids)
    # change as u wants
    max_attempts = 5
    attempt = 0
    while (attempt < max_attempts):
        time.sleep(0.2)
        wrong_ids = get_wrong_ids(wrong_ids)

        if (len(wrong_ids) == 0):
            break
        elif (count != len(wrong_ids)):
            print("\n YEE, is works!!!\n")
        else:
            print("\n Isn't works!!!\n")
            attempt += 1
        count = len(wrong_ids)

    for wrong_id in wrong_ids:
        print("Wrong id: ", wrong_id)
