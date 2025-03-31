def stack(s):
    new_string = s.split()

    res = []
    for i in new_string:
        res.append(i)
    return ' '.join(res[::-1])


s = 'I am Rahul'
result = ' '.join(s.split()[::-1])
print(result, stack(s))


