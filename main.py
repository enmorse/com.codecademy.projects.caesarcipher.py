alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?!' "
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh " \
          "syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! " \
          "iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""

for letter in message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value + 10) % 26]
    else:
        translated_message += letter
print(translated_message)
