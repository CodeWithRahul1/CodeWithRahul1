s = "This is a python language"
new_string = s.split()
res = [word for word in new_string if len(word) % 2 == 0]

even_words = filter(lambda w: len(w) %2 == 0, new_string)
print(' '.join(res), ' '.join(even_words))