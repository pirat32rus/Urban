def single_root_words(root_word, *other_words):
    return [word for word in other_words if root_word.lower() in word.lower()]

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('книг', 'книга', 'книги', 'стол', 'книжный', 'журнал')

print(result1)
print(result2)
