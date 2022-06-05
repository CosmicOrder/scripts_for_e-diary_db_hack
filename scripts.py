import re
from random import randint, choice

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, \
    Commendation


def fix_marks(schoolkid: str):
    if schoolkid:
        try:
            child_marks = Mark.objects.get(
                schoolkid__full_name__icontains=schoolkid)
            child_bad_marks = child_marks.filter(points__in=[2, 3])
            for child_bad_mark in child_bad_marks:
                child_bad_mark.points = randint(4, 5)
                child_bad_mark.save()
        except ObjectDoesNotExist:
            print('Ученика с таким именем не существует. Уточните '
                  'правильность написания имени')
        except MultipleObjectsReturned:
            print('Учеников с таким именем слишком много, уточните фамилию '
                  'ученика')
    else:
        return 'Пустая строка не принимается, введите имя и фамилию'


def remove_chastisements(schoolkid: str):
    if schoolkid:
        try:
            child = Schoolkid.objects.get(full_name__icontains=schoolkid)
            comments = Chastisement.objects.filter(schoolkid=child)
            comments.delete()
        except ObjectDoesNotExist:
            print('Ученика с таким именем не существует. Уточните '
                  'правильность написания имени')
        except MultipleObjectsReturned:
            print('Учеников с таким именем слишком много, уточните фамилию '
                  'ученика')
    else:
        return 'Пустая строка не принимается, введите имя и фамилию'


praise_text = """
    1. Молодец!
    2. Отлично!
    3. Хорошо!
    4. Гораздо лучше, чем я ожидал!
    5. Ты меня приятно удивил!
    6. Великолепно!
    7. Прекрасно!
    8. Ты меня очень обрадовал!
    9. Именно этого я давно ждал от тебя!
    10. Сказано здорово – просто и ясно!
    11. Ты, как всегда, точен!
    12. Очень хороший ответ!
    13. Талантливо!
    14. Ты сегодня прыгнул выше головы!
    15. Я поражен!
    16. Уже существенно лучше!
    17. Потрясающе!
    18. Замечательно!
    19. Прекрасное начало!
    20. Так держать!
    21. Ты на верном пути!
    22. Здорово!
    23. Это как раз то, что нужно!
    24. Я тобой горжусь!
    25. С каждым разом у тебя получается всё лучше!
    26. Мы с тобой не зря поработали!
    27. Я вижу, как ты стараешься!
    28. Ты растешь над собой!
    29. Ты многое сделал, я это вижу!
    30. Теперь у тебя точно все получится!"""

praise_phrases = re.split('\n\s+\d+\.\s+', praise_text)
praise_phrases = list(filter(None, praise_phrases))

subjects = [
    'Краеведение',
    'География',
    'Математика',
    'Музыка',
    'Физкультура',
    'Изобразительное исскуство',
    'Технология',
    'Русский язык',
    'Литература',
    'Обществознание',
    'Иностранный язык',
    'Биология',
    'История',
    'Основы безопасности жизнедеятельности (ОБЖ)',
]


def create_commendation(schoolkid: str, subject: str):
    if schoolkid:
        if subject in subjects:
            try:
                child = Schoolkid.objects.get(full_name__icontains=schoolkid)
                target_lessons = Lesson.objects.filter(
                    year_of_study=child.year_of_study,
                    group_letter=child.group_letter,
                    subject__title__icontains=subject)

                target_lesson = choice(target_lessons)

                Commendation.objects.create(text=choice(praise_phrases),
                                            created=target_lesson.date,
                                            schoolkid=child,
                                            subject=target_lesson.subject,
                                            teacher=target_lesson.teacher)
            except ObjectDoesNotExist:
                print('Ученика с таким именем не существует. Уточните '
                      'правильность написания имени')
            except MultipleObjectsReturned:
                print('Учеников с таким именем слишком много, уточните фамилию '
                      'ученика')
        else:
            return 'Такого прдемета не существует, проверьте правильность ' \
                   'написания предмета'
    else:
        return 'Пустая строка не принимается, введите имя и фамилию'
