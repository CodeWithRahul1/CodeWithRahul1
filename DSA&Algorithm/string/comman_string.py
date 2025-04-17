def method(s):
    uniq_string = ''
    for i in s[0]:
        if i not in uniq_string:
            uniq_string += i

    result = ''
    for ch in uniq_string:
        found_in_all = True
        for word in s[1:]:
            if ch not in word:
                found_in_all = False
                break
        if found_in_all:
            result += ch

    return result

s = ['bcfg', 'abcdece', 'abdce']
print(method(s))




























































# def method(s):
#     uniq_string = ''
#     res = s[0]

    
#     for i in res:
#         found = False
#         for j in uniq_string:
#             if i == j:
#                 found = True
#                 break
#         if not found:
#             uniq_string += i
    
#     result = ''
#     for ch in uniq_string:
#         is_common = True
#         for word in s[1:]:
#             match = False
#             for c in word:
#                 if c == ch:
#                     match = True
#                     break
#             if not match:
#                 is_common = False
#                 break
#         if is_common:
#             result += ch

#     return result


# s = ['bcfg', 'abcdece', 'abdce', ]
# print(method(s))