s = input("Bвeдитe строку:\n")
s = s.upper()
k = 0
for i in range(0, len(s)):
    if s.count(s[i]) > k:
        k = s.count(s[i])
print(k)
