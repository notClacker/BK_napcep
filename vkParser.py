import vk
import time

from tokens import me_user_token
from tokens import me_service_token

def get_text_from_file(file_name):
    text = ""
    with open(file_name, 'r') as file:
        for i in file.read():
            text = text + i
    return text


def get_ids_from_file(file_name, start_substr, end_substr):
    text = get_text_from_file(file_name)
    ids = []
    start_index = 0;
    while (True):
        start_index = text.find(start_substr, start_index)
        if (start_index == -1):
            break

        start_index +=  len(start_substr)
        end_index = text.find(end_substr, start_index)
        id = text[start_index : end_index]
        ids.append(id)
    return ids

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
        #print(id, ' ', end = '')
    return ids

def get_wrong_ids(ids):
    wrong_ids = []

    # max_wrong_time = 0
    # is_work = False
    for id in ids:
        print("ID : ", id)
        last_worked_time = time.time()
        last_not_worked_time = time.time()
        try:
            response = api.users.get(user_ids=id, fields='city')
            if (len(response) > 0):
                man_processing(response[0])

            # if (not is_work):
            #     is_work = not is_work
            #
            #     last_worked_time = time.time()
            #     print(last_not_worked_time - time.time())
            #     last_not_worked_time = time.time()

        except vk.exceptions.VkAPIError:
            time.sleep(0.1)
            wrong_ids.append(id)

            # if (is_work):
            #     is_work = not is_work
            #
            #     last_not_worked_time = time.time()
            #     print(last_worked_time - time.time())
            #     last_worked_time = time.time()

    return wrong_ids


# the app user token from the https://vkhost.github.io/   -> KateMobile
# https://oauth.vk.com/blank.html#access_token=&(THERE IS WILL BE YOUR TOKEN)&expires_in=0&user_id=&(you user id)
# Example: user_token = '123456789qwertyuiop'
user_token = me_user_token

session = vk.Session(access_token=user_token)
api = vk.API(session, v=5.112)

# the app service token     https://vk.com/editapp?id=&(app id)&section=options
#service_token = me_service_token

# the substrings beetween both where contaiments user id
start_substr = '<div class="Entity__aside"><a href="/'
end_substr = '"'

# Test for working of the session
# response = api.users.get(user_ids=1, fields='city')
# print(response[0])

chat_id = 1
ids = get_ids_from_chat(chat_id)

# file with HTML dump on page of group members
# file_name = 'rowData.txt'
# ids = get_ids_from_file(file_name, start_substr, end_substr)

wrong_ids = []
#wrong_ids = get_wrong_ids(ids)

if (len(wrong_ids) > 0):
    count = len(wrong_ids)
    # change as u wants
    max_attempts = 5
    attempt = 0
    while (attempt < max_attempts):
        time.sleep(0.2)
        #wrong_ids = get_wrong_ids(wrong_ids)
        some_ids = [wrong_ids[-1]]
        wrong_ids = get_wrong_ids(some_ids)

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
