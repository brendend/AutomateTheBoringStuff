import random

messages = ['It is certain.',
    'It is decidedly so.',
    'Yes definitely.',
    'Reply is hazy, try agian.',
    'Ask again later',
    'Concentrate and ask again.',
    'My reply is no.',
    'Outlook is not good.',
    'Absolutely not.',
    'Fuck no.']


while True:   
        print('Ask the magic 8 ball a question')
        question = input()
        print(messages[random.randint(0, len(messages) - 1)])
        if question == "end":
            break