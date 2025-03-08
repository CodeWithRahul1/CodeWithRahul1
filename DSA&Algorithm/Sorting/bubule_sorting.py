

def method(li):
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i]> li[j]:
                li[i], li[j] = li[j], li[i]
    return li



li = [4,3,5,1,2,6]
print(method(li))