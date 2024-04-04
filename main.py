import random

with open('google-10000-english.txt') as f:
    words = f.readlines()

words = [line.strip() for line in words]

new_words = []

while True:
    print(f"== TOTAL DE NOVAS PALAVRAS: {len(new_words)} ==")

    with open('known_words.txt') as f:
        known_words = f.readlines()

    known_words = [line.strip() for line in known_words]

    # pega as palavras
    count = 0
    round_words = []
    while True:
        random_number = random.randint(0, len(words) - 1)

        if count >= 10:
            break
        elif words[random_number] in known_words:
            pass
        else:
            round_words.append(words[random_number])
            count += 1

    # adicione todas as palavras conhecidas na palavra
    with open('known_words.txt', 'a') as f:
        for round_word in round_words:
            f.write(round_word + '\n')


    # imprime as palavras
    for i, round_word in enumerate(round_words):
        print(i, round_word)

    # pega as palavras que nao sei
    not_known_words = str(input("numbers: ")).split(" ")

    # se for 444 acabou
    if not_known_words[0] == "444":
        break
    elif not_known_words[0] == "":
        pass
    else:
        not_known_words = [int(i) for i in not_known_words]

        for not_known_word_index in not_known_words:
            new_words.append(round_words[not_known_word_index])


print(f"== NOVAS PALAVRAS: {", ".join(new_words)} ==")

