def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
       if ('@' not in recipient or '@' not in sender or not recipient.endswith((".com", ".ru", ".net"))
            or not sender.endswith((".com", ".ru", ".net"))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient} '
              f'Текст сообщения: {message}')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Привет,это администратор!', 'ivanPop@ov.ru')
