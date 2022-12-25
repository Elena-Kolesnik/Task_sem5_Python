# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def compression_algorithm(string_specified):
    string = ''
    count = 1
    element = string_specified[0]
    for i in range(1, len(string_specified)):
        if string_specified[i] == element:
            count += 1
        else:
            string = string + str(count) + element
            element = string_specified[i]
            count = 1
    return string

def recovery_algorithm(compressed_string):
    string_specified = ''
    elements = ''
    for i in range(len(compressed_string)):
        if compressed_string[i].isdigit():
            elements += compressed_string[i]
        else:
            string_specified += compressed_string[i] * int(elements)
        elements = ''
    print(string_specified)
    return string_specified


with open('specified.txt', 'w') as date:
    date.write('QQQQQQQWWWWWWWWEEEEEERTTTTTTTTTYYY')

with open('specified.txt', 'r') as date:
    string_specified = date.readline()

with open('specified.txt', 'r') as date:
    string_specified = date.read()

with open('compression.txt', 'w') as file:
    compressed_string = compression_algorithm(string_specified)
    file.write(compressed_string)

print('Восстановленные данные: ' + string_specified)
print('Сжатые данные: ' + compression_algorithm(string_specified))                      