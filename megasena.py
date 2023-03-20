import random

number_mega = []
total_lines = 1

while len(number_mega) < 10:
    random_number = random.randrange(1, 60)
    if random_number not in number_mega:
        number_mega.append(random_number)

try:
    with open('numeros da mega.txt', 'r') as file:
        lines = file.readlines()
        total_lines = len(lines) + 1
        
    with open('numeros da mega.txt', 'a') as file:
        if total_lines == 1:
            file.write(f'Mega {total_lines}: {sorted(number_mega)}')
            file.close()
        else:
            file.write(f'\nMega {total_lines}: {sorted(number_mega)}')
            file.close()
        
except:
    with open('numeros da mega.txt', 'a') as file:
        file.write(f'Mega {total_lines}: {sorted(number_mega)}')
        file.close()