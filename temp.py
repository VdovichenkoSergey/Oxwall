import json

with open('messages.txt', 'r', encoding="utf-8") as input1:
    # list1 = [
    #     'There is a new message',
    #     'There is a new message There is a new message There is a new message There is a new message There is a new message There is a new message There is a new message There is a new message There is a new message There is a new message',
    #     '!@#$%^&*()_+',
    #     'There   is',
    #     'Новое сообщение?*/-:;"-='
    # ]
    # input1.writelines(["%s\n" % item for item in list1])
    # input1.close()

    list1 = json.loads(input1.read())

    print(list1)