def check_email(email):
    if '@' not in email or '.' not in email:
        print('НЕТ')
    else:
        for char in email:
            if not (char.isalnum() or char in ['@', '.', '_']):
                print('НЕТ')
        print('ДА')


email = input()
check_email(email)
