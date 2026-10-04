#!/usr/bin/env python3


STANDARD_DELIMITED: str = ' '

INVOKE: dict[str, str] = {
    'Cold_Snap': '111',
    'Ghost_Walk': '112',
    'Ice_Wall': '113',
    'EMP': '222',
    'Tornado': '221',
    'Alacrity': '223',
    'Sun_Strike': '333',
    'Forge_Spirit': '331',
    'Meteor': '332',
    'Deafening_Blast': '123',
}


def encode(text: str):
    result: list[str] = []

    for skill in text.split(STANDARD_DELIMITED):
        if skill in INVOKE:
            result.append(INVOKE[skill])
        else:
            result.append(skill)

    return STANDARD_DELIMITED.join(result)


def decode(text: str):
    result: list[str] = []

    for number in text.split(STANDARD_DELIMITED):
        all_is_fine: bool = False

        for skill in INVOKE:
            if INVOKE[skill] == number:
                result.append(skill)
                all_is_fine = True

        if not all_is_fine:
            result.append(number)

    return STANDARD_DELIMITED.join(result)


if __name__ == '__main__':
    choice: str = input(
        'Приготовьтесь к битве, выбирай: 1 - если пишешь название скилла,'
        ' 2 - если "кастуешь": '
    ).strip()

    if choice == '1':
        text: str = input(
            'Напиши один или несколько скиллов (скилл в 2 слова через _): '
        ).strip()

        if not text:
            print('Безмолвие')
        else:
            print('QWE:', encode(text))

    elif choice == '2':
        text: str = input(
            'Лех, готовь санстрайк: '
        ).strip()

        if not text:
            print('Далеко до Миракла..')
        else:
            print('Прокаст:', decode(text))

    else:
        print('GG, WP')
