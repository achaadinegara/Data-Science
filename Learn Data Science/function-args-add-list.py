"""
Membuat fungsi
* berfungsi untuk membungkus semua argument yang ada kedalam list. Aksesnya adalah sebagaimana kita mengakses list
** berfungsi untuk membungkus semua keyword argument (key=val) kedalam dictionary. Aksesnya adalah sebagaimana kita mengakses dictionary
Memanggil fungsi
* berfungsi untuk membuka list menjadi argument.
** berfungsi untuk membuka dictionary menjadi keyword argument (key=val)
"""

def gibberish(b):
    """concatenate strings in *args together"""

    hodgepoge = ""

    for word in b:
        hodgepoge += word
    
    return hodgepoge

one_word = gibberish('luke')
many_words = gibberish('tasya','amanda','adinegara')

print(one_word)
print(many_words)