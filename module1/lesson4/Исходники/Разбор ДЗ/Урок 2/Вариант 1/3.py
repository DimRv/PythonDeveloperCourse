"""Спросите пользователя, идет ли дождь. Преобразуйте его ответ к нижнему
регистру. Если пользователь ответит «yes», спросите, ветрено ли на улице. Если
пользователь ответит «yes» и на второй вопрос, выведите сообщение «It is too
windy for an umbrella»; в противном случае выведите сообщение «Take an
umbrella». Если же пользователь не дал положительного ответа на первый вопрос,
выведите сообщение «Enjoy your day»"""

answer = input("Идет ли дождь? Yes/No\n").lower()
if answer=='yes':
    answer = input("ветрено ли на улице? Yes/No\n").lower()
    if answer == 'yes':
        print('Itn is too windy for an umbrella');
    else:
        print('Take an umbrella')
else: print('Enjoy your day')
