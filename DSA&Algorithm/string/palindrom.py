

def palindrom1(s, n):
    
    hslf_string = n//2
    if s == s[::-1]:
        print('Plindrom string')
    if s[hslf_string:] == s[:hslf_string]:
                            print('Symentric string')
    else:
        return False


def palindrom(s, n):
        
        new_String = ''
        for i in s:
                new_String = i + new_String
        if new_String == s:
                return True
        else:
            return False
        
def twoPointer(s, n):
        i, j = 0, n-1
        pal = True
        while i < j:
                if s[i] != s[j]:
                        pal = False
                        break
                i += 1
                j -= 1
        if pal == True:
                return pal
        else: 
            return pal







s = "abaab"
n = len(s)
print(palindrom(s, n))
print(twoPointer(s, n))
