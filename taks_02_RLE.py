""" Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в
отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). """

in_file = 'rle_encode.txt'
out_file = 'rle_decode.txt'


def encode_file():
    with open(in_file, 'r') as file:
        txt = file.read().strip()
    print(txt)

    index, index2 = 0, 0
    encoded_txt = ''
    while index < len(txt):
        encoded_txt += txt[index]
        count = 0
        while index2 < len(txt):
            if txt[index2] == txt[index]:
                index2 += 1
                count += 1
            else:
                break
        index = index2
        encoded_txt += str(count)
    print(encoded_txt)


def decode_file():
    with open(out_file, 'r') as file:
        txt = file.readline().strip()
    print(txt)
    decoded_txt = ''
    index = 0
    while index < len(txt):
        index2 = index + 1
        while index2 < len(txt) and txt[index2].isdigit():
            index2 += 1
        decoded_txt += txt[index] * int(txt[index + 1:index2])
        index = index2
    print(decoded_txt)


if __name__ == '__main__':
    print('Кодирование файла', in_file)
    encode_file()
    print()
    print('Декодирование файла', out_file)
    decode_file()