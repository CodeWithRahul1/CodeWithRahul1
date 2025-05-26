def longest_palindromsubstring(s):
    res = ''
    for i in range(len(s)):
        left1,right1=expandAroundCenter(s,i,i)
        if right1-left1+1>len(res):
            res =s[left1:right1+1]
        left2,right2=expandAroundCenter(s,i,i+1)
        if right2-left2+1>len(res):
            res =s[left2:right2+1]
    return res


def expandAroundCenter(s,left,right):
    while left >=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    return left+1,right-1



s = "babad"
print(longest_palindromsubstring(s))
