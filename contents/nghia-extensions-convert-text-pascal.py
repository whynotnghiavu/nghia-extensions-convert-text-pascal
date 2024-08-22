import pyperclip
from unidecode import unidecode
# pip install pyperclip
# pip install unidecode

def adapter(input_str):
    words = unidecode(input_str).split()
    output = [word.capitalize() for word in words]
    return ''.join(output)


text = pyperclip.paste()
print(f"Chuyển: {text}")
output = adapter(text)
print(f"Thành: {output}")
pyperclip.copy(output)
