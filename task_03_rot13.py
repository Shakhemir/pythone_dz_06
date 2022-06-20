alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def Rot13(txt: str, decode=False):
    shift = 13 if not decode else -13
    result = ''
    for char in txt:
        if char in alfavit_EU:
            index = alfavit_EU.index(char)
            new_index = (index + shift) % len(alfavit_EU)
            result += alfavit_EU[new_index]
        elif char in alfavit_RU:
            index = alfavit_RU.index(char)
            new_index = (index + shift) % len(alfavit_RU)
            result += alfavit_RU[new_index]
        else:
            result += char
    return result


if __name__ == '__main__':
    # text = 'Я КУРСАНТ SOLDIER'
    text = 'ПРИШЕЛ УВИДЕЛ ПОБЕДИЛ'
    encode_text = Rot13(text)
    print(encode_text)
    decode_text = Rot13(encode_text, decode=True)
    print(decode_text)