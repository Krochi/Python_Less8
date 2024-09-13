#Задание1

# with open('numbers.txt', 'r', encoding='UTF-8') as infile:
#     total_sum = 0
#     for line in infile:
#         numbers = line.split()
#         for num in numbers:
#             total_sum += int(num)
# with open('answer.txt', 'w', encoding='UTF-8') as outfile:
#     outfile.write(str(total_sum))
#
#
#
#
# #Задание2
#
# with open('zen.txt', 'r') as file:
#     lines = file.readlines()
#     for line in reversed(lines):
#         print(line.strip())



#Задание3


# with open('first_tour.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
# if len(lines) < 2:
#     raise ValueError("Файл должен содержать хотя бы одно значение для K и одного участника.")
#
# K = int(lines[0].strip())
#
# participants = []
#
# for line in lines[1:]:
#     line = line.strip()
#
#     if not line:
#         continue
#
#     try:
#         surname, name, score = line.split()
#         score = int(score)
#     except ValueError:
#         print(f"Некорректная строка: '{line}', пропускаем её.")
#         continue
#
#     if score > K:
#         participant = {
#             'surname': surname,
#             'initial': name[0] + '.',
#             'score': score
#         }
#         participants.append(participant)
#
# participants_sorted = sorted(participants, key=lambda p: p['score'], reverse=True)
#
# with open('second_tour.txt', 'a', encoding='utf-8') as file:
#     file.write(str(len(participants_sorted)) + '\n')
#     for idx, participant in enumerate(participants_sorted, 1):
#         file.write(f"{idx}) {participant['initial']} {participant['surname']} {participant['score']}\n")

#Задание4


# from collections import defaultdict
#
# with open('text.txt', 'r') as file:
#     text = file.read().lower()
#
# letter_count = defaultdict(int)
# total_letters = 0
#
# for char in text:
#     if 'a' <= char <= 'z':
#         letter_count[char] += 1
#         total_letters += 1
#
# letter_frequencies = {}
#
# for letter, count in letter_count.items():
#     letter_frequencies[letter] = count / total_letters
#
# sorted_frequencies = sorted(letter_frequencies.items(), key=lambda x: (-x[1], x[0]))
#
# with open('analysis.txt', 'w') as file:
#     for letter, freq in sorted_frequencies:
#         file.write(f"{letter} {freq:.3f}\n")

#Задание5

import zipfile
from collections import Counter

with zipfile.ZipFile('voina-i-mir.zip', 'r') as z:
    file_list = z.namelist()

    text_file_name = None
    for file_name in file_list:
        if file_name.endswith('.txt'):
            text_file_name = file_name
            break

    if text_file_name:
        with z.open(text_file_name) as f:
            text = f.read().decode('utf-8')

letter_counter = Counter()

for char in text:
    if char.isalpha():
        letter_counter[char] += 1

sorted_letters = sorted(letter_counter.items(), key=lambda x: (-x[1], x[0]))

for letter, count in sorted_letters:
    print(f"{letter}: {count}")
