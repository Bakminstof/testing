def revers_words_in_text(text):
    text = list(text)
    text.reverse()
    start = 0
    for i_letter in range(len(text)):
        if text[i_letter] == ' ':
            start = i_letter + 1
        text.insert(start, text[i_letter)
        text.pop(i_letter + 1)
    return ''.join(text)

# text = 'Спасибо за подписку'
# print(revers_words_in_text(text))