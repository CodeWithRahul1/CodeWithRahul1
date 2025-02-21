def method(str1):
    mapping= {}

    for word in str1:
        sorted_word = ''.join(sorted(word))
        

        if sorted_word not in mapping:
            mapping[sorted_word] = []
        mapping[sorted_word].append(word)

    result = list(mapping.values())
    return result


str1 = ['rat', 'art', 'tar', 'eat', 'tea', 'bat']
print(method(str1))