class sampleclass:
    count = 0

    def increse(self):
        sampleclass.count += 1


s1 = sampleclass()
s1.increse()
print(s1.count)
s1.increse()
print(s1.count)
print(sampleclass.count)